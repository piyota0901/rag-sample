# rag-sample

# 前提条件
- WSL2(Ubuntu)
- Docker
- Python(3.11.5)

## 起動コマンド
```bash
$ poetry run python -m llama_cpp.server --model ${PWD}/llm/models/llama-2-7b-chat.Q4_K_M.gguf
$ poetry run uvicorn main:app --host=0.0.0.0 --port=3000 
```

## OpenAI API互換サーバー
使用しているノートPCは、GPUを搭載していないので[llama-cpp-python](https://github.com/abetlen/llama-cpp-python?tab=readme-ov-file#openai-compatible-web-server)を使う。

起動コマンド
```bash
$ cd <workspace>
$ poetry run python -m llama_cpp.server --model ${PWD}/llm/models/llama-2-7b-chat.Q4_K_M.gguf
llama_model_loader: loaded meta data with 19 key-value pairs and 291 tensors from /home/tatsuro/development/rag-sample/llm/models/llama-2-7b-chat.Q4_K_M.gguf (version GGUF V2)
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = llama
llama_model_loader: - kv   1:                               general.name str              = LLaMA v2
・・・
llm_load_tensors: offloaded 0/33 layers to GPU
llm_load_tensors:        CPU buffer size =  3891.24 MiB
warning: failed to mlock 74469376-byte buffer (after previously locking 0 bytes): Cannot allocate memory
Try increasing RLIMIT_MLOCK ('ulimit -l' as root).
```

確認コマンド ※数十秒かかる
```bash
$ curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "something",
    "messages": [{"role": "user", "content": "Hello! What is your name?"}]
  }'
{"id":"chatcmpl-95861344-9fbe-47a8-a95f-55593da80369","object":"chat.completion","created":1705742444,"model":"something","choices":[{"index":0,"message":{"content":"  Hello! My name is LLaMA, I'm a large language model trained by a team of researcher at Meta AI. 😊","role":"assistant"},"finish_reason":"stop"}],"usage":{"prompt_tokens":18,"completion_tokens":34,"total_tokens":52}}% 
```

サンプル
```python
import openai

openai.api_key = "EMPTY"                        # ←これが必要
openai.base_url = "http://localhost:8000/v1/"   # ←これが必要

model = "vicuna-7b-v1.5"
prompt = "Once upon a time"

# create a completion
completion = openai.completions.create(model=model, prompt=prompt, max_tokens=64)
# print the completion
print(prompt + completion.choices[0].text)

# create a chat completion
completion = openai.chat.completions.create(
  model=model,
  messages=[{"role": "user", "content": "Hello! What is your name?"}]
)
# print the completion
print(completion.choices[0].message.content)
```