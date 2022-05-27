import json

class Config:
    def __init__(self):
       self.controls = {}
       self.video = {}
       self.config_files_path = './config/config_files'
       self.setup_video_config()

    def setup_video_config(self):
        with open(f'{self.config_files_path}/video.json') as f:
            video_data = json.load(f)
        self.video['resolution'] = tuple(map(lambda x: int(x), video_data['resolution'].split('x')))

    def _resolution_to_string(self):
        return f"{str(self.video['resolution'][0])}x{str(self.video['resolution'][1])}"

    def update_video_config(self):
        json_dict = {}
        json_dict['resolution'] = self._resolution_to_string()
        with open(f'{self.config_files_path}/video.json','w', encoding='utf-8') as f:
            json.dump(json_dict, f)