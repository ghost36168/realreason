{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "arrA=[8,10,12,44,63]\n",
    "arrB=[2,3,20,106,144]\n",
    "arrC=[]\n",
    "while i<len(arrA) or j<len(arrB):\n",
    "    if i<len(arrA) and j<len(arrB):\n",
    "        if arrA[i]<arrB[j]:\n",
    "            arrC[i+j]=arrA[i]\n",
    "            i=i+1\n",
    "        else:\n",
    "            arrC[i+j]=arrB[j]\n",
    "            j=j+1\n",
    "    elif i<len(arrA) and j= len(arrB):\n",
    "        arrC[i+j+1:]=arrA[i+1:]\n",
    "    else:\n",
    "        arrC[i+j+1:]=arrB[j+1:]\n",
    "    i=i+1\n",
    "    j=j+1"
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
