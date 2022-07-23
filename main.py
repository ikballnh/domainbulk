from traceback import print_tb
from unittest import result
import requests
from requests.structures import CaseInsensitiveDict
from concurrent.futures import ThreadPoolExecutor
import time

def save(filename, text):
  more_lines = [text, '']
  with open(filename, 'a', encoding="utf8") as f:
    f.writelines('\n'.join(more_lines))


def check(domain):
    myobj = "links%5B%5D="+domain+"&url=1&domain=0"
    headers = CaseInsensitiveDict()
    headers["Host"] = "www.softo.org"
    headers["Cookie"] = 'Cookie: ci_session=a%3A5%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%221621b4f8b730598b956052e8f3f61545%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A14%3A%22180.214.233.90%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A111%3A%22Mozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F103.0.0.0%20Safari%2F537.36%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1658395734%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3B%7D013be57eba806f37005df90977f73fa4; _ga=GA1.2.629443986.1658395739; _gid=GA1.2.68655283.1658395739; __gads=ID=5823f1c3700a480f-220bc37744d50042:T=1658395736:RT=1658395736:S=ALNI_MbvnO_J_NeDqvewVj8zOc7w_GfyuQ; __gpi=UID=000007edeef81b32:T=1658395736:RT=1658395736:S=ALNI_MbFLRcEb5Cy5PPpNUlXBMxkybuZ6Q; _clck=1x6w5rg|1|f3c|0; __cf_bm=WiQwWPgtwqi1LGL7c6mGXu5dch_XYylDpeMOQ0r_5y8-1658395737-0-ASXu1CfmOWw6eR8ee8r6E+1qekGMjEdgx4MCbmEyUvgmN46WPk8XRWrlQX/NGPa/AzFHJ/29GxKMivCIAemKEV90vkwVGCdEdNimOcYwJLOHNVJHLqR2KVTqJDspYgUx3Q==; _clsk=l8j19h|1658395741591|1|1|f.clarity.ms/collect'
    headers["Accept"] = "*/*" 
    headers["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8" 
    headers["X-Requested-With"] = "XMLHttpRequest" 
    headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36" 
    headers["Accept-Encoding"] = "gzip, deflate" 
    headers["Accept-Language"] = "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7" 

    try:
        r = requests.post("https://www.softo.org/ajax/dacheck", data=myobj, headers=headers, timeout=30)
        result = r.json()
        
        da = (result[0]['all']['domain_auth'])
        pa = (result[0]['all']['page_auth'])
        mozrank = (result[0]['all']['m_rank'])
        backlinks = (result[0]['all']['total_links'])
        result = "[+] "+domain+" | DA: "+str(da)+" | PA: "+str(pa)+" | MRANK: "+str(mozrank)+" | BACKLINKS: "+str(backlinks)+""
        save("result.txt", result)
        print(result)
    
    except:
        result = "[-] "+domain+" | ERROR, TRY AGAIN => Saved in errorlist.txt"
        save("errorlist.txt", result)
        print(result)


intro = """
  ____  _   _ _     _  __  ____   ___  __  __    _    ___ _   _    ____ _   _ _____ ____ _  _______ ____  
 | __ )| | | | |   | |/ / |  _ \ / _ \|  \/  |  / \  |_ _| \ | |  / ___| | | | ____/ ___| |/ / ____|  _ \  
 |  _ \| | | | |   | ' /  | | | | | | | |\/| | / _ \  | ||  \| | | |   | |_| |  _|| |   | ' /|  _| | |_) |
 | |_) | |_| | |___| . \  | |_| | |_| | |  | |/ ___ \ | || |\  | | |___|  _  | |__| |___| . \| |___|  _ < 
 |____/ \___/|_____|_|\_\ |____/ \___/|_|  |_/_/   \_\___|_| \_|  \____|_| |_|_____\____|_|\_\_____|_| \_\                                                                                                       
"""
print(intro)
print("BULK DOMAIN FAST CHECKER (DA, PA, MOZA RANK, BACKLINK)")
print("With multi threading")
print("Author: Ikbal Nur Hakim")
print("Error ? Contact me https://web.facebook.com/ikbal.nurhakim.798/")

file = input("\nEnter list domain [ex: domain.txt]: ")
threads = input("How many threads [recommendation: 50]: ")
print("Saved in result.txt")

text_file= open(file, 'r', encoding="utf8")
data=text_file.read()
dsplit = data.split("\n")

start_time = time.time()

pool = ThreadPoolExecutor(max_workers=int(threads))
for isi in dsplit:
    a = isi.replace("https://", "")
    domain = a.replace("/", "")
    pool.submit(check,domain)

pool.shutdown(wait=True)

totalsemua = len(dsplit)
waktu = "--- %s seconds ---" % (time.time() - start_time)
print ("\nfinished  "+str(totalsemua)+" domain in "+str(waktu)+"")
