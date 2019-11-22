{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "class TreeNode(object):\n",
    "    def __init__(self,x):\n",
    "        self.val=x\n",
    "        self.left=None\n",
    "        self.right=None"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Solution(object):\n",
    "    def insert(self,root,val):\n",
    "        newNode=TreeNode(val)\n",
    "        if newNode:\n",
    "            if val> newNode:\n",
    "                if self.right ==None:\n",
    "                    self.right =val\n",
    "                else:\n",
    "                    return False\n",
    "            else:\n",
    "                if self.left == None:\n",
    "                    self.left = val\n",
    "                else:\n",
    "                    return False\n",
    "            \n",
    "        else:\n",
    "            self.root=root"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def delete(self,root,target):\n",
    "        \n",
    "def search(self,root,target):\n",
    "    if root==self.target:\n",
    "        return self.target\n",
    "    else:\n",
    "        return None\n",
    "        \n",
    "def modify(self,root,target,new_val)"
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
