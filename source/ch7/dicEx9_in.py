a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118','email':"naver"}
isNameExist='name' in a
isEmailExist='email' in a
print(isNameExist,isEmailExist)
if isNameExist:
    val =a['name']
    print(val)
if isEmailExist:
    val =a['email']
    print(val)