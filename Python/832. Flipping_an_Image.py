class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in range(0,len(image)):
            image[i]=[1 if X==0 else 0 for X in image[i][::-1]]
        return image