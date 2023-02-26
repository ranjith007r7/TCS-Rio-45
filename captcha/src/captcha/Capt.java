package captcha;

import java.util.Random;

public class Capt {
	public String getC() {
		char data[] = {
				'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V'
                ,'W','X','Y','Z','1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i',
                'j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', '!','@','#','$','%','^','&','*','+'
		};
		char index[]= new char[6];
		Random r =new Random();
		
		int i=0;
		for(i=0;i<(index.length);i++) {
			int ran =r.nextInt(data.length);
			index[i]=data[ran];
		}
		return new String(index);
		}
	public static void main(String[] args) {
		Capt c =new Capt();
		System.out.println(c.getC());
	}

}
