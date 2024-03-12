import sys
from llama_cpp import Llama
from pureples.hyperneat.hyperneat import create_phenotype_network

# HyperNEATの設定
genome = "gene/xss-cheatsheet.txt"  # 進化させたいニューラルネットワークのジェノムファイルのパス
config = "hyperneat_config/hyperneat_config.json"  # HyperNEATの設定ファイルのパス

# ニューラルネットワークの生成
network = create_phenotype_network(genome, config)

# 軽量LLMの設定
model_path = "llm_models/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf"  # 軽量LLMモデルのパス
llm = Llama(model_path=model_path, verbose=False)

# ニューラルネットワークからの出力を軽量LLMの入力として使用
input_vector = [0.5, -0.2, 0.8]  # 例としての入力ベクトル
output_vector = network.activate(input_vector)

# 出力ベクトルを文字列に変換
output_str = " ".join(map(str, output_vector))

# 軽量LLMを使用して自然言語のPayloadを生成
prompt = f"<user>\n{output_str}\n<assistant>\n"
output = llm(prompt, max_tokens=40)
payload = output['choices']["text"]

print(f"Generated Payload: {payload}...")
