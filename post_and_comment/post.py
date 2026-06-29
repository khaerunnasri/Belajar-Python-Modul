import requests
from post_and_comment import comment

def menu_post():
    while True:
        print("=====================")
        print(" MENU POST ")
        print("1. Tampilkan Semua Post")
        print("2. Tampilkan Post Berdasarkan ID")
        print("3. Keluar")

        pilihan = int(input("Masukkan Pilihan Menu : "))
        if pilihan == 1:
            tampilkan_semua_post()
        elif pilihan == 2:
            post_id = int(input("Masukkan ID Post : "))
            tampilkan_post_berdasarkan_id(post_id)
            comment.menu_comment(post_id)
        elif pilihan == 3:
            print("=== Program Post Selesai ===")
            break


def ambil_semua_post(): # Ambil semua post di internet
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        list = response.json()
        return list
    else:
        print("Gagal mengambil data")
        return []

def tampilkan_semua_post(): # tampilkan semua post yang diambil di internet semua post berdasarkan id dan title
    list_post = ambil_semua_post()
    for post in list_post:
        print("==============")
        print(f"Tampilkan id: {post['id']}")
        print(f"Tampilkan title: {post['title']}")

def tampilkan_post_berdasarkan_id(post_id): # Tampilkan post berdasarkan id 
    response =  requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
    if response.status_code == 200:
        data = response.json()
        print("==============")
        print(f"ID Post: {data['id']}")
        print(f"Title: {data['title']}")
        print(f"Body: {data['body']}")
    else:
        print("Gagal mengambil data")
        