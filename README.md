# HyperNEATAndLLMMeetsXSSPayloadGene
Hyper NEAT And LLM Meets XSS Payload Generate

<!-- ABOUT THE PROJECT -->
## About The Project

本リポジトリはHyperNEAT(Hyper-Neural Evolution Algorithm)とLLM(Large Language Model)を使用したStoredXSSで使用されるPayload生成の研究に使用される．
HyperNEATは，ニューラルネットワークの構造を進化的アルゴリズムを用いて最適化するための手法である．LLMは大量のテキストデータを学習して文章を生成するためのモデルである．
StoredXSSとはXSSの一種である．攻撃者が標的のWebサーバやデータベースに悪意あるスクリプトであるPayloadを埋め込むことで，他の利用者がそのコンテンツにアクセスした際にPayloadが実行される．
HyperNEATとLLMを組み合わせることで，より高度なPayload生成が可能になると予測する．

pureples (https://github.com/ukuleleplayer/pureples)[https://github.com/ukuleleplayer/pureples]
TinyLlama-1.1B-Chat-v1.0-GGUF (https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/blob/main/README.md)[https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/blob/main/README.md]

<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

## Installation

1. Clone the repo
   ```sh
   git clone https://github.com/yusch/HyperNEATAndLLMMeetsXSSPayloadGene
   ```

<!-- USAGE EXAMPLES -->
## Usage

```sh
$ sudo docker image build -t hyperneat .
$ sudo docker run -it hyperneat python main.py

or

$ docker run -it --rm --name HyperNEATAndLLMMeetsXSSPayloadGene -v "$PWD":/usr/src/myapp -w /usr/src/myapp python:3 python main.py

# after running
$ sudo docker container ls -a
$ sudo docker container prune
$ sudo docker images
$ sudo docker rmi $(sudo docker images -a -q)
```

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request