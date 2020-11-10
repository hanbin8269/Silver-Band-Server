# Silver-Band-Server
Silver-Band-Server
## 인증

- POST `/users/auth/register/`  # 회원가입

    request

    ```json
    {
    	"username" : "hanbin",
    	"email" : "gksqls0128@gmail.com",
    	"password" : "0128gksqls"
    }
    ```

    response

    {

    ```json
    # 이미 계정이 존재할떄
    {
      "email": [
        "user with this email address already exists."
      ]
    }

    # 성공했을때
    {
      "user": {
        "id": 4,
        "username": "hanbin",
        "email": "gksqls012@gmail.com"
      }
    }
    ```
- POST `/users/auth/login/` # 로그인

    request

    ```json
    {
    	"email" : "gksqls0128@gmail.com",
    	"password" : "0128gksqls"
    }
    ```

    response

    ```json
    {
      "user": {
        "id": 3,
        "username": "hanbin",
        "email": "gksqls0128@gmail.com"
      },
      "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MywiZW1haWwiOiJna3NxbHMwMTI4QGdtYWlsLmNvbSJ9.plj8NDRkg52ntBC0TgTPzNFOk5HBArF3BakO-BiLRvI"
    }
    ```
    ## 유저 정보

- PUT `/users/<user_id:int>/wearer/` # 착용자 정보 변경

    request

    ```json
    {
    	"name" : "habi",
    	"age" : 59,
    	"sex" : "male",
    	"address" : "광주광역시 광산구 신촌동 상무대로 312"
    }
    ```

    response

    ```json
    {
    	"wearer" : {
    		"name" : "habi",
    		"age" : 59,
    		"sex" : "male",
    		"address" : "광주광역시 광산구 신촌동 상무대로 312"
    	}
    }
    ```

- POST `/users/<user_id:int>/wearer/` # 착용자 정보 생성

    request

    ```json
    {
    	"name" : "habi",
    	"age" : 59,
    	"sex" : "male",
    	"address" : "광주광역시 광산구 신촌동 상무대로 312"
    }
    ```

    response

    ```json
    {
    	"wearer" : {
    		"name" : "habi",
    		"age" : 59,
    		"sex" : "male",
    		"address" : "광주광역시 광산구 신촌동 상무대로 312"
    	}
    }
    ```

- GET `/users/<user_id:int>/` # 보호자 조회

    response

    ```json
    {
      "user": {
        "id": 4,
        "username": "hanbin",
        "email": "gksqls012@gmail.com"
      }
    }
    ```

- GET `/users/<user_id:int>/wearer/` # 착용자 조회

    response

    ```json
    {
    	"wearer" : {
    		"id" : 1,
    		"name" : "habi",
    		"age" : 59,
    		"sex" : "male",
    		"address" : "광주광역시 광산구 신촌동 상무대로 312"
    	}
    }
    ```
