## Before

1. Python 코딩
    - 흩어진 문자열 합치는 함수 만들기
    - strings = ['I', 'love', 'python !']
        - [리스트 자료형](https://wikidocs.net/14)
    - 넘어온 리스트 자료형에 담긴 문자들을 하나로 합쳐서 리턴
    - 리턴은 [문자열 자료형](https://wikidocs.net/13)인 **"I love python !"**
    ```python
    def join(str):
        # .. TODO
        return 0

    strings = ['I', 'love', 'python !']
    result = join(strings)

    print(result) # It will be: "I love python !"
    ```
1. Python 코딩
    - 1 ~ 10 까지 더하기
    - one_to_ten은 1~10까지 담긴 [리스트](https://wikidocs.net/14)
    - 리스트에 담긴 1~10을 순회하면서 모든 값들을 더한 후 리턴
        - [for](https://wikidocs.net/58)
        - [while](https://wikidocs.net/56)
    - 리턴은 [숫자형](https://wikidocs.net/12)인 **55**

    ```python
    def sum10(number):
        # .. TODO
        return 0

    one_to_ten = range(1,11)
    ```


## After
Before의 내용 1,2 번 정리해서 PR 날리기
함수의 리턴 값 확실히!