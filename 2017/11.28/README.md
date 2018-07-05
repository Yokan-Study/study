# 2017.11.28

## pip

### What is pip?
파이썬 패키지 관리자

#### package
![package](http://weknowyourdreams.com/images/package/package-12.jpg)
> 실행 가능한 완성된 S/W 묶음

#### package manager
패키지를 관리해주는 일련의 S/W
패키지를 사용하려면 설치, 버전관리, 삭제 등 기본적인 설치 과정이 필수적으로 필요하다.

추가적으로 테스트-빌드, 의존성 관리 등 관리 포인트가 많다.

이러한 복잡한 패키지의 사용을 쉽게 관리해주는 것이 **package manager**

#### python package manager
**pip**
Python 언어로 작성되고 Python 환경에서 실행가능한 패키지들을 관리하는 package manager

pip를 이용하면, Python 기본 내장 클래스, 함수들로 부족한 기능을 보완할 수 있다.

### Install
Python 설치시 기본으로 설치됨

### Why pip?
Excel, HTTP 등등 모든 요구사항을 Python으로 해결할 수 없음
Python 개발자들이 모든 패키지를 만들어서 Python에 기본으로 내장시키면 좋을 수도 있지만, Python 자체가 너무 무거워짐

따라서, 패키지로 만들어서 필요한 사용자만 설치해서 사용하게 제공

## openpyxl
https://openpyxl.readthedocs.io/en/default/

Python에서 Excel을 사용할 수 있는 패키지

**Install:**
```bash
$ pip install openpyxl
```

output:
```bash
Collecting openpyxl
  Downloading openpyxl-2.4.9.tar.gz (157kB)
    100% |################################| 163kB 219kB/s
Collecting jdcal (from openpyxl)
  Downloading jdcal-1.3.tar.gz
Collecting et_xmlfile (from openpyxl)
  Downloading et_xmlfile-1.0.1.tar.gz
Installing collected packages: jdcal, et-xmlfile, openpyxl
  Running setup.py install for jdcal ... done
  Running setup.py install for et-xmlfile ... done
  Running setup.py install for openpyxl ... done
Successfully installed et-xmlfile-1.0.1 jdcal-1.3 openpyxl-2.4.9
```

### Usage
- https://openpyxl.readthedocs.io/en/default/tutorial.html#
- http://www.hanul93.com/openpyxl-basic/
- http://pythonstudy.xyz/python/article/405-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%97%91%EC%85%80-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0