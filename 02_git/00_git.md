# Git

## 1. git과 git hub

git: 프로젝트 버전관리 소프트웨어

git hub: git 기반 클라우드 저장소

## 2. 커밋 해시, 태그

커밋 해시: 각 버전에 지칭된 고유 ID

태그: 포스트잇과 비슷한 역할, 보통 버전 번호를 붙임

## 3. revert

commit 되돌리기. 기존 버전은 모두 유지하며 이전 commit을 다음 commit으로 복사한다. 


많이 사용하면 헷갈릴 수 있으므로 적절할 때 가끔 써야한다. 일반적으로 대형 프로젝트에서 git 전문가가 주로 사용한다.

commit 이름은 기존에 주어진 revert로 사용하는 게 일반적이다.

## 4. reset

선택한 commit까지 브랜치를 초기화한다.

1. soft-reset: 저장소에서만 삭제
2. mixed-reset: 스테이지 및 저장소에서 삭제
3. hard-reset: 작업 디렉토리에서마저 삭제

> 실무에서 일반적으로 hard-reset을 사용한다. git은 간단하게 사용하는 게 좋으며, 복잡한 작업 시 꼬일 가능성이 높기 때문이다.

## 5. stash

작업을 했지만 commit하지 않은 상태에서, 작업물을 임시 보관하는 기능.

마찬가지로 꼬여서 에러 발생 가능성을 높일 수 있으므로, 1개만 쌓아 놓는게 바람직하다. stash 적용 후 지워주는 게 좋다.

## 6. branch

여러 버전을 동시에 관리하기 위한 기능.

최초의 branch는 master-branch로 이름이 정해져 있다. 깃허브에서는 main-branch라고 부른다.

이름은 목적에 맞게 부여하는 게 좋다.

1. HEAD

    현재 작업 중인 commit

2. checkout

    HEAD를 바꾸는 행위

## 7. merge

1. fast-forward merge

    두 개의 branch 중 하나가 변경 사항이 없을 경우, 변경 사항이 있는 branch를 없는 branch의 마지막 commit 뒤에 붙인다.

2. merge

    두 브랜치를 병합한 새로운 commit을 생성한다.

## 8. conflict

병합하려는 두 branch가 서로 같은 내용을 다르게 수정한 상황.

어떤 branch의 내용을 반영할 지 사용자가 직접 선별하고, 다시 commit 해야 한다.

따라서 가능한 서로 다른 branch에서는 별개의 파일을 변경하는 게 좋다.

## 9. 원격 저장소

git과 원격 저장소와의 상호작용

1. clone

    원격 저장소를 local로 복제하기

2. push

    local에서 원격 저장소에 밀어넣기

3. fetch

    원격 저장소의 변경 사항을 일단 가져만 오기. 병합하지 않음.

4. pull

    fetch + 병합. 원격 저장소를 가져와서 병합하기.

## 10. 설치파일

설치 파일 및 DB는 git에 넣지 않는다.

1. `.gitignore`

    git hub에 올리지 않을 파일의 확장자 명을 적는 파일.
    
    [toptal](https://www.toptal.com/developers/gitignore/)에서 `python, django, venv, windows` 등의 키워드를 입력하여 올리지 않을 파일들을 정리해줌.

    직접 입력할수도 있음.

2. `freeze`

가상 환경에 설치된 프로그램들의 버전을 나타내는 파일 이름.

가상 환경에서 프로그램 버전 불러오기

`pip freeze > requiremenets.txt`

가상 환경에서 버전에 따라 프로그램 한번에 설치하기

`pip install -r requirements.txt`
