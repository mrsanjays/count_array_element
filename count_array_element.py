class Solution:
    @staticmethod
    def count_array_element(array):
        mx=float('-inf')
        for element in array:
            if element>mx:
                mx=element
        count=0
        for element in array:
            if element==mx:
                count+=1
        return len(array)-count
if __name__ == '__main__':
    array=list(map(int,input().split()))
    ob=Solution()
    print(ob.count_array_element(array))