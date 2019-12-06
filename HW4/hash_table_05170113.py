{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#參考資料 https://www.youtube.com/watch?v=oqzStHk36PI&feature=youtu.be\n",
    "from Crypto.Hash import MD5\n",
    "h=MD5.new()\n",
    "class ListNode:\n",
    "    def __init__(self,val):\n",
    "        self.val=val\n",
    "        self.next=None\n",
    "class MyHashSet:\n",
    "    def __init__(self,capacity=5):\n",
    "        self.capacity=capacity\n",
    "        self.data = [None] * capacity\n",
    "    def add(self,key: int):\n",
    "        idx =key% self.capacity\n",
    "        node =self.data[idx]\n",
    "        if node==None:\n",
    "            node=key\n",
    "        else:\n",
    "            node.next=ListNode(key)\n",
    "    def contains(self,key:int):\n",
    "        idx =key% self.capacity\n",
    "        if key == node:\n",
    "            return True\n",
    "        else:\n",
    "            return False"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
