import requests
from bs4 import BeautifulSoup
from markdownify import markdownify

        
headers = {'Accept': 'application/json'}

base_url = "https://www.leagueoflegends.com/page-data/"
patchs_notes_menu_url = '/news/tags/patch-notes/'
end_url = "page-data.json"
view_url = "https://www.leagueoflegends.com/"

        
class PatchNote:
    
    def __init__(self, previous : int = 0, lang : str = 'en-gb'):
        
        self.menu_request_url : str = base_url+lang+patchs_notes_menu_url+end_url
        
        try:
            patch_notes_menu_data = requests.get(self.menu_request_url, headers=headers).json()
        except (Exception):
            raise PatchNoteException(f"Patch notes menu data request error for url: {self.menu_request_url}")
        
        try:
            patch_note_url = patch_notes_menu_data['result']['data']['articles']['nodes'][previous]['url']['url']
        except (Exception):
            raise PatchNoteException(f"Patch note url not found in patch notes menu data")
        
        self.link = view_url + lang + patch_note_url 
        self.patch_request_url : str = base_url+lang+patch_note_url+end_url
        
        try:
            patch_note_data = requests.get(self.patch_request_url, headers=headers).json()
        except (Exception):
            raise PatchNoteException(f"Patch note data request error for url: {reself.patch_request_urlquest_url}")
        
        try:
            self.title = patch_note_data['result']['data']['all']['nodes'][0]['description']
        except (Exception):
            raise PatchNoteException(f"Patch note title not found")
        
        soup = BeautifulSoup(patch_note_data['result']['data']['all']['nodes'][0]['patch_notes_body'][0]['patch_notes']['html'], 'html.parser')
        

        try:
            self.description : str = markdownify(str(soup.blockquote),  heading_style="ATX").replace('>','').strip().replace("\n \n", "\n")
        except (Exception):
            raise PatchNoteException(f"Not able to retrieve desription from html")
        
        try:
            self.overview_image : str = soup.find(attrs={"class": "skins cboxElement"}).img.get('src')
        except (Exception):
            self.overview_image : str = 'https://images.contentstack.io/v3/assets/blt731acb42bb3d1659/bltf06237d0ebbe32e0/5efc23abee48da0f762bc2f2/LOL_PROMOART_4.jpg'

            
        
    def __str__(self):
        return f"{self.title}\n({self.link})\n\n{self.description}\n\n{self.overview_image}\n\n{'-'*10}\n\nMenu url: {self.menu_request_url}\n\nPatch request url: {self.patch_request_url}"
        
        

class PatchNoteException(Exception):
        
    def __init__(self, msg : str = None):
        super().__init__(msg)


        
if __name__ == '__main__':
    patch = PatchNote()
    print(patch)

    