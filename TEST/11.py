"""void main(){
    int max = getMax(readKeyboard());
    print(max);
}"""

'''int getMax(list a){
    len = a.length();
    maxCurrent = 0;
    for i from 0 to len step 1:
        for j from i to len step 1:
            sum = 0;
            for k from i to j step 1:
                sum = sum + a[k];
            maxCurrent = max(maxCurrent, max);
}'''
def GetMax(a):
    len1 = len(a)
    maxCurrent = 0
    for i in range(len1+1):
        for j in range(i,len1+1):
            sum = 0
            for k in range(i, j):
                sum = sum + a[k]
            print(sum)
        maxCurrent = max(maxCurrent,sum)
    return maxCurrent




a = [1,2,3,4,5]
print(GetMax(a))
