books = []
# {("book_id":"1"),("book_name":"파이썬책")}
while True:
    print("== 도서관리 시스템 ==")
    print("1. 도서등록")
    print("2. 전체 도서 조회")
    print("3. 도서 삭제")
    print("q. 종료")

    selected_menu = input("메뉴를 선택>>")
    if selected_menu == "1":
        book_id = input("책 아이디를 입력하세요>>")
        book_name = input("책 이름을 입력하세요>>")
        is_duplicated = False
        for book in books:
            if book["book_id"] == book_id:
                is_duplicated = True
                print("책 아이디가 중복됩니다 다시 입력하세요")
                break
            if book["book_name"] == book_name:
                is_duplicated = True
                print("책 이름이 중복됩니다 다시 입력하세요")
                break
        if is_duplicated:
            continue
        book_new = {"book_id": book_id, "book_name": book_name}
        books.append(book_new)
        pass
    elif selected_menu == "2":
        book_id = input("조회할 책 아이디를 입력하세요")
        book_name = input("조회할 책을 입력하세요")
        if not books:
            print("입력된 책이 없습니다")
            continue
        for book in books:
            book_id = book["book_id"]
            book_name = book["book_name"]
            print(f"조회된 책이름은 {book_name}이고 아이디는 {book_id}입니다")
        pass
    elif selected_menu == "3":
        delete_id = input("삭제할 도서의 id를 입력하세요:")
        for book in books:
            if book["book_id"] == delete_id:
                books.remove(book)
                print("조회한 책이 삭제되었습니다")
                break
            if delete_id not in books:
                print("삭제할 책이 없습니다")
                break
        pass
    elif selected_menu == "q":
        print("프로그램 종료")
        break
    else:
        print("잘못된 입력입니다 다시 입력하세요>>")
        continue

