def get_seed(filename):
    try:
        f = open(filename, 'rb')
        file_content = f.read()
        f.close()
        ok=0
        file_content=str(file_content)
        for i in file_content:
            if i=='0':
                ok+=1
        return ok
    except:
        return "NOO!!!"