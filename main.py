{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "import os \n",
    "import csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "#import csv\n",
    "pol_data_01=os.path.join(\"election_data_1.csv\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "#variables, change for other data set\n",
    "votes_total=0\n",
    "vestal_total=0\n",
    "torres_total=0\n",
    "seth_total=0\n",
    "cordin_total=0\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "#open csv, count votes\n",
    "with open(pol_data_01) as csvfile:\n",
    "    csvreader= csv.reader(csvfile)            \n",
    "    for row in csvreader:\n",
    "        votes_total = votes_total + 1\n",
    "    #candidates.append(row[2])           \n",
    "        \n",
    "        if row[2] == \"Vestal\":\n",
    "            vestal_total=vestal_total+1\n",
    "        elif row[2] == \"Torres\":  \n",
    "            torres_total=torres_total+1\n",
    "        elif row[2] == \"Seth\":  \n",
    "            seth_total=seth_total+1\n",
    "        elif row[2] == \"Cordin\":  \n",
    "            cordin_total=cordin_total+1\n",
    "            \n",
    "            "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "#winning candidate\n",
    "candidates_dict={\"Vestal\":vestal_total,\"Torres\":torres_total, \"Seth\":seth_total,\"Cordin\":cordin_total}\n",
    "winner=max(candidates_dict, key=candidates_dict.get)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "#format counts\n",
    "vestal='{:.2%}'.format(vestal_total/votes_total)\n",
    "torres='{:.2%}'.format(torres_total/votes_total)\n",
    "seth='{:.2%}'.format(seth_total/votes_total)\n",
    "cordin='{:.2%}'.format(cordin_total/votes_total)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "#print in a text file\n",
    "with open(\"PyPoll.txt\", \"w\") as text_file:\n",
    "    print(\"```\", file=text_file)\n",
    "    print(\"Election Results\", file=text_file)\n",
    "    print(\"-------------------------\", file=text_file)\n",
    "    print (\"Total Votes:\" + str(votes_total), file=text_file)\n",
    "    print(\"-------------------------\", file=text_file)\n",
    "    print(\"Vestal:\"+ vestal +\"(\"+str(vestal_total)+\")\", file=text_file)\n",
    "    print(\"Torres:\"+ torres +\"(\"+str(torres_total)+\")\", file=text_file)\n",
    "    print(\"Seth:\"+ seth +\"(\"+str(seth_total)+\")\", file=text_file)\n",
    "    print(\"Cordin:\"+ cordin +\"(\"+str(cordin_total)+\")\", file=text_file)\n",
    "    print(\"-------------------------\", file=text_file)\n",
    "    print(\"Winner:\" + str(winner), file=text_file)\n",
    "    print(\"-------------------------\", file=text_file)\n",
    "    print(\"```\", file=text_file)\n",
    "\n"
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
   "version": "3.6.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
