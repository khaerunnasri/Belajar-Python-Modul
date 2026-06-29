from post_and_comment import post 

if __name__== "__main__":
    while True:
        print("=== PROGRAM POST COMMENT ===")
        print("1. Daftar Post")
        print("2. Keluar")
        print("=== PROGRAM POST COMMENT ===")

        pilihan = int(input("Pilihan : "))
        if pilihan == 1:
            post.menu_post()
        elif pilihan == 2:
            print("=== Program Post Comment selesai ===")
            break
        

