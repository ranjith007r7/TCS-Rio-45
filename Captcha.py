import random

class Captcha:
    def getC(self):
        data = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V',
                'W','X','Y','Z','1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i',
                'j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', '!','@','#','$','%','^','&','*','+']
        index = []
        for i in range(6):
            ran = random.randint(0, len(data) - 1)
            index.append(data[ran])
        return ''.join(index)

if __name__ == '__main__':
    c = Captcha()
    print(c.getC())
