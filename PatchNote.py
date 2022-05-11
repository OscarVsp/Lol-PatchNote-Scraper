import requests
from bs4 import BeautifulSoup
from markdownify import markdownify

        
headers = {'Accept': 'application/json'}

base_url = "https://www.leagueoflegends.com/page-data/"
patchs_notes_menu_url = '/news/tags/patch-notes/'
end_url = "page-data.json"
view_url = "https://www.leagueoflegends.com/"

langs = ['fr-fr','en-gb']

        
class PatchNote:
    
    def __init__(self, previous : int = 0, lang : str = 'en-gb'):
        if lang not in langs:
            print(f"lang '{lang}' is not officially supported. I will to get the same way than for 'en-gb' and warn you in case of error.")
                
        
        self.menu_request_url : str = base_url+lang+patchs_notes_menu_url+end_url
        
        try:
            patch_notes_menu_data = requests.get(self.menu_request_url, headers=headers).json()
        except (Exception):
            raise PatchNoteException(f"Patch notes menu data request error for url: {self.menu_request_url}")
        
        try:
            patch_note_url = patch_notes_menu_data['result']['data']['articles']['nodes'][previous]['url']['url']
        except (Exception):
            raise PatchNoteException(f"Patch note url not found in patch notes menu data.")
        
        self.link = view_url + lang + patch_note_url 
        self.patch_request_url : str = base_url+lang+patch_note_url+end_url
        
        try:
            patch_note_data = requests.get(self.patch_request_url, headers=headers).json()
        except (Exception):
            raise PatchNoteException(f"Patch note data request error for url: {reself.patch_request_urlquest_url}")
        
        try:
            self.title = patch_note_data['result']['data']['all']['nodes'][0]['description']
        except (Exception):
            raise PatchNoteException(f"Title not found")
        
        if lang in langs:
            try:
                if lang == 'fr-fr':
                    print(patch_note_data['result']['data']['all']['nodes'][0]['title'])
                    self.label : str = patch_note_data['result']['data']['all']['nodes'][0]['title'].split(' ')[3]
                    self.season_number : int = 0
                    self.patch_number : int = 0
                elif lang == 'en-gb':
                    self.label : str = patch_note_data['result']['data']['all']['nodes'][0]['title'].split(' ')[1]
                    self.season_number : int = int(self.label.split('.')[0])
                    self.patch_number : int = int(self.label.split('.')[1])
            except (Exception):
                raise PatchNoteException(f"Label, season_number and patch_number could not be retrieved from title.")
        else:
            try:
                self.label : str = patch_note_data['result']['data']['all']['nodes'][0]['title'].split(' ')[1]
                self.season_number : int = int(self.label.split('.')[0])
                self.patch_number : int = int(self.label.split('.')[1])
            except (Exception):
                print(f"Label, season_number and patch_number could not be retrieved from title. This can be due to the unsupported lang. Default value are used instead.")
                self.label : str = "NA"
                self.season_number : int = 0
                self.patch_number : int = 0
        
        soup = BeautifulSoup(patch_note_data['result']['data']['all']['nodes'][0]['patch_notes_body'][0]['patch_notes']['html'], 'html.parser')
        

        try:
            self.description : str = markdownify(str(soup.blockquote),  heading_style="ATX").replace('>','').strip().replace("\n \n", "\n")
        except (Exception):
            raise PatchNoteException(f"Not able to retrieve desription from html")
        
        try:
            self.overview_image : str = soup.find(attrs={"class": "skins cboxElement"}).img.get('src')
        except (Exception):
            raise PatchNoteException(f"Not able to overview image from html")

            
        
    def __str__(self):
        return f"{self.season_number}.{self.patch_number}\n{self.title}\n({self.link})\n\n{self.description}\n\n{self.overview_image}\n\n{'-'*10}\n\nMenu url: {self.menu_request_url}\n\nPatch request url: {self.patch_request_url}"
        
        

class PatchNoteException(Exception):
        
    def __init__(self, msg : str = None):
        super().__init__(msg)


        
if __name__ == '__main__':
    patch = PatchNote(previous = 0, lang = 'fr-fr')
    print(patch)


    