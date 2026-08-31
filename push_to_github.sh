
#!/bin/bash

set -e

echo ""

echo "=== 깃허브 저장소 주소를 정확히 입력하세요 ==="

echo "형식 예시: https://github.com/YouJung8800/credit-robot.git"

echo "https://github.com/YouJung8800/credit-robot.git"

echo ""

read -p "주소 입력: " REPO_URL

case "$REPO_URL" in

  *" "*)

    echo "!!! 에러: 공백이 있어요. 다시 실행해서 정확히 입력하세요."; exit 1 ;;

  *"("*|*")"*)

    echo "!!! 에러: 괄호는 지우고 주소만 입력해야 해요."; exit 1 ;;

esac

if echo "$REPO_URL" | LC_ALL=C grep -q '[^ -~]'; then

    echo "!!! 에러: 한글이 섞여 있어요. 저장소를 영문 이름으로 다시 만드세요."; exit 1

fi

if ! echo "$REPO_URL" | grep -Eq 'github\.com/[A-Za-z0-9_-]+/[A-Za-z0-9_.-]+'; then

    echo "!!! 에러: 이건 프로필 주소예요, 저장소 주소가 아니에요."

    echo "!!! github.com/new 에서 저장소를 먼저 만들고, 그 저장소 페이지의"

    echo "!!! 초록 'Code' 버튼을 눌러 나오는 HTTPS 주소를 복사하세요."

    exit 1

fi

echo "OK: 주소 형식 정상 확인됨 -> $REPO_URL"

if [ -z "$(git config --global user.email)" ]; then

    read -p "깃허브 가입 이메일: " GIT_EMAIL

    git config --global user.email "$GIT_EMAIL"

fi

if [ -z "$(git config --global user.name)" ]; then

    read -p "이름: " GIT_NAME

    git config --global user.name "$GIT_NAME"

fi

[ ! -d ".git" ] && git init

git branch -M main

echo "__pycache__/

*.pyc" > .gitignore

git add .

git commit -m "가정용 신용체크 로봇" || echo "(커밋할 변경사항 없음, 계속 진행)"

git remote remove origin 2>/dev/null || true

git remote add origin "$REPO_URL"

git push -u origin main

echo ""

echo "=== 완료! $REPO_URL 에서 확인하세요 ==="

