// ≈≈–ÚÀ„∑®÷ÆSleepSort

public class SleepSort {
    
    public static void main(String[] args) {
    		int[] arr = {2, 1, 5, 6, 3};
    		for (int i : arr){
    		new Thread(){
    			@Override
    			public void run(){
    				try{
    					Thread.sleep(i);
    					System.out.println(i);
    				}catch (InterruptedException e) {
						e.printStackTrace();
					}
    			}
    		}.start();	
    		}
      }
}