class Solution:
    def simplifyPath(self, path: str) -> str:
        ruta = []
        for i in path.split('/'):
            if i != '' and i != '.' and i != '..':
                ruta.append(i) 
            elif i == '..' and len(ruta) > 0:
                    ruta.pop()   
        return '/'+ ('/').join(ruta)
