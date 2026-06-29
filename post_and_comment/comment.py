import requests

def menu_comment(post_id):
    while True:
        print("=====================")
        print(" MENU COMMENT ")
        print(f"1. Tampilkan Semua Comment  dari Post {post_id}")
        print(f"2. Tampilkan Comment Berdasarkan ID Comment dari Post {post_id}")
        print("3. Keluar")

        pilihan = int(input("Masukkan Pilihan : "))
        if pilihan == 1:
            tampilkkan_semua_comment(post_id)
        elif pilihan == 2:
            comment_id = int(input("Masukkan ID Coment : "))
            tampilkan_comment_berdasarkan_id(post_id, comment_id)
        elif pilihan == 3:
            print("=== Program Comment Selesai ===")
            break

def ambil_semua_comment(post_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}/comments")
    if response.status_code == 200:
        list = response.json()
        return list
    else:
        print("Gagal mengambil data")
        return []
    
def tampilkkan_semua_comment(post_id):
    list_comment = ambil_semua_comment(post_id)
    for comment in list_comment:
        print("====================")
        print(f"ID Comment: {comment['id']}")
        print(f"Name: {comment['name']}")
        
def tampilkan_comment_berdasarkan_id(post_id, comment_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/comments/{comment_id}") 
    if response.status_code == 200:
        data = response.json()

        if data["postId"] == post_id:
            print("====================")
            print(f"ID Comment: {data['id']}")
            print(f"Name: {data['name']}")
            print(f"Body: {data['body']}")
        else:
            print("ID Comment tidak sesuai")
    else:
        print("Gagal mengambil data")
        
       