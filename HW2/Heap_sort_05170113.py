{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "k=0\n",
    "alist=[2,6,9,8,7,3,4]\n",
    "left=alist[2*k+1]\n",
    "right=alist[2*k+2]\n",
    "central=alist[k]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "final=(len(alist)-2)/2\n",
    "while k < final:\n",
    "    if alist[2*k+1] > alist[k] and alist[2*k+2]>alist[k]:\n",
    "        if alist[2*k+1] > alist[2*k+2]:\n",
    "            temp=alist[k]\n",
    "            alist[k]=alist[2*k+1]\n",
    "            alist[2*k+1]=temp\n",
    "        else :\n",
    "            temp=alist[k]\n",
    "            alist[k]=alist[2*k+2]\n",
    "            alist[2*k+2]=temp\n",
    "    elif alist[2*k+1] > alist[k] and alist[2*k+2] < alist[k]:\n",
    "        temp=alist[k]\n",
    "        alist[k]=alist[2*k+1]\n",
    "        alist[2*k+1]=temp\n",
    "    elif alist[2*k+2] > alist[k] and alist[2*k+1] < alist[k]:\n",
    "        temp=alist[k]\n",
    "        alist[k]=alist[2*k+2]\n",
    "        alist[2*k+2]=temp\n",
    "    else:\n",
    "        print(alist)\n",
    "        print(central)\n",
    "        print(left)\n",
    "        print(right)\n",
    "    k=k+1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[9, 8, 4, 6, 7, 3, 2]"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "alist"
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
