{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 6, 9, 8, 7, 3, 4]\n",
      "1\n",
      "[2, 6, 9, 8, 7, 3, 4]\n",
      "2\n",
      "[2, 6, 9, 8, 7, 3, 4]\n",
      "3\n"
     ]
    }
   ],
   "source": [
    "k=0\n",
    "alist=[2,6,9,8,7,3,4]\n",
    "left=alist[2*k+1]\n",
    "right=alist[2*k+2]\n",
    "central=alist[k]\n",
    "final=(len(alist)-1)/2\n",
    "while k <= final:\n",
    "    if left > central and right>central:\n",
    "        if left > right:\n",
    "            temp=alist[k]\n",
    "            central=left\n",
    "            left=temp\n",
    "            print(alist)\n",
    "        else :\n",
    "            temp=central\n",
    "            central=right\n",
    "            right=temp\n",
    "    elif left > central and right < central:\n",
    "        temp=alist[k]\n",
    "        alist[k]=left\n",
    "        left=temp\n",
    "    elif right > central and left < central:\n",
    "        temp=central\n",
    "        central=right\n",
    "        right=temp\n",
    "    else:\n",
    "        print(alist)\n",
    "        print(k)\n",
    "    k=k+1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
