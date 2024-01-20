import injector
import openai

openai.api_key = "DUMMY"
openai.base_url = "http://localhost:8000/v1/"

from mypackage.dataaccess.configs import get_modules
from mypackage.presentation.schemas import StartupSchema
from mypackage.service.startups import StartupsService

injector_instance = injector.Injector(modules=[get_modules()])

def search_startups(keyword: str, limit: int) -> list[StartupSchema]:
    """スタートアップ企業を検索する
    """
    startup_service = injector_instance.get(StartupsService)
    startups = startup_service.find(text=keyword, limit=limit)
    # StartupSchemaに変換
    startups_schemas = []
    for startup in startups:
        startups_schemas.append(
            StartupSchema(
                id=startup.id,
                score=startup.score,
                name=startup.name,
                alt=startup.alt,
                description=startup.description,
                link=startup.link,
                city=startup.city,
                images=startup.images,
            )
        )
    return startups_schemas


def search_by_rag(query: str) -> str:
    """スタートアップ企業をRAG検索する
    """
    startup_service = injector_instance.get(StartupsService)
    startups = startup_service.find(text=query, limit=5)
    
    joined_company_name_and_alt = [
                                    startup.name \
                                    + " " \
                                    + startup.alt \
                                    + startup.description
                                    for startup in startups
                                ]
    
    for_dump = [
                {
                    "name": startup.name,
                    "alt": startup.alt,
                    "description": startup.description,
                }
                for startup in startups
    ]
    with open("for_dump.json", "w") as f:
        import json
        json.dump(for_dump, f, indent=4)
    context = "\n\n".join(joined_company_name_and_alt)
    
    metaprompt = f"""
    You are a great search assistant about startup companies. 
    Answer the following question using the provided context. 
    If you can't find the answer, do not pretend you know it, but answer "I don't know".
    Please list in bullet points.

    Question: {query.strip()}

    Context: 
    {context.strip()}

    Answer:
    """
    
    completion = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": metaprompt},
        ],
    )

    return completion.choices[0].message.content