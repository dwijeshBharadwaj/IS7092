{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "a73e00f9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'satyanadella': {'data': [{'id': '20571756', 'name': 'Satya Nadella', 'username': 'satyanadella'}]}, 'tim_cook': {'data': [{'id': '1636590253', 'name': 'Tim Cook', 'username': 'tim_cook'}]}, 'ajassy': {'data': [{'id': '26389359', 'name': 'Andy Jassy', 'username': 'ajassy'}]}, 'reedhastings': {'data': [{'id': '15241557', 'name': 'Reed Hastings', 'username': 'reedhastings'}]}, 'ramonlaguarta': {'data': [{'id': '1026414410452152320', 'name': 'Ramon Laguarta', 'username': 'ramonlaguarta'}]}, 'cristianoamon': {'data': [{'id': '234930762', 'name': 'Cristiano R. Amon', 'username': 'cristianoamon'}]}, 'ChuckRobbins': {'data': [{'id': '16810559', 'name': 'Chuck Robbins', 'username': 'ChuckRobbins'}]}, 'Pgelsinger': {'data': [{'id': '3339261074', 'name': 'Pat Gelsinger', 'username': 'PGelsinger'}]}, 'ArvindKrishna': {'data': [{'id': '24204488', 'name': 'Arvind Krishna', 'username': 'ArvindKrishna'}]}, 'LisaSu': {'data': [{'id': '836224570013138944', 'name': 'Lisa Su', 'username': 'LisaSu'}]}, 'sasan_goodarzi': {'data': [{'id': '2598339625', 'name': 'Sasan Goodarzi', 'username': 'sasan_goodarzi'}]}, 'acce': {'data': [{'id': '14153794', 'name': 'Alex Chriss', 'username': 'acce'}]}, 'scottfarkas': {'data': [{'id': '14243030', 'name': 'Scott Farquhar', 'username': 'scottfarkas'}]}, 'dittycheria': {'data': [{'id': '14773334', 'name': 'Dev Ittycheria', 'username': 'dittycheria'}]}}\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "import pandas as pd\n",
    "\n",
    "# Hard-code the bearer token\n",
    "bearer_token = 'AAAAAAAAAAAAAAAAAAAAANE9twEAAAAAbj6SVx%2FKE1hExDTy3me2W8pPmmc%3D7xQvh90geD9eWnPN5pBNLShnMq0Vieyxur3v6ARPNe4elqj9ZZ'\n",
    "\n",
    "# Endpoint URL\n",
    "url = \"https://api.twitter.com/2/users/by\"\n",
    "\n",
    "# Load the Excel file and get the list of usernames\n",
    "handle_df = pd.read_excel('/Users/dwijesh/Desktop/ProjectFiles/twitterHandles.xlsx')\n",
    "ceo_list = handle_df['CeoHandle'].tolist()\n",
    "\n",
    "# Define the headers with the bearer token for authentication\n",
    "headers = {\n",
    "    'Authorization': f'Bearer {bearer_token}'\n",
    "}\n",
    "\n",
    "# Dictionary to store JSON responses\n",
    "user_details = {}\n",
    "\n",
    "# Iterate over the list of usernames\n",
    "for username in ceo_list:\n",
    "    params = {\n",
    "        'usernames': username,\n",
    "        'user.fields': 'id'\n",
    "    }\n",
    "    response = requests.get(url, headers=headers, params=params)\n",
    "\n",
    "    # Check for a successful response\n",
    "    if response.status_code == 200:\n",
    "        user_details[username] = response.json()\n",
    "    else:\n",
    "        print(f\"Failed to retrieve details for {username}: {response.status_code}\")\n",
    "        print(response.text)\n",
    "\n",
    "# Print the dictionary containing the JSON responses\n",
    "print(user_details)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "4f4cc1ac",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['20571756',\n",
       " '1636590253',\n",
       " '26389359',\n",
       " '15241557',\n",
       " '1026414410452152320',\n",
       " '234930762',\n",
       " '16810559',\n",
       " '3339261074',\n",
       " '24204488',\n",
       " '836224570013138944',\n",
       " '2598339625',\n",
       " '14153794',\n",
       " '14243030',\n",
       " '14773334']"
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "handle_df['Name'] = handle_df['CeoHandle'].apply(lambda x: user_details[x]['data'][0]['name'] if x in user_details else None)\n",
    "handle_df['ID'] = handle_df['CeoHandle'].apply(lambda x: user_details[x]['data'][0]['id'] if x in user_details else None)\n",
    "\n",
    "# Define the path where the Excel file will be saved\n",
    "file_path = '/Users/dwijesh/Desktop/ProjectFiles/twitterHandles_with_details.xlsx'\n",
    "\n",
    "# Save the DataFrame to an Excel file without the index\n",
    "handle_df.to_excel(file_path, index=False)\n",
    "\n",
    "# Display the DataFrame (optional, for Jupyter Notebook display)\n",
    "handle_id = handle_df['ID'].to_list()\n",
    "handle_id"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 119,
   "id": "662248cf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Tweets saved to /Users/dwijesh/Desktop/ProjectFiles/omega2.xlsx\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "import json\n",
    "from datetime import datetime, timedelta\n",
    "import pandas as pd\n",
    "import os\n",
    "\n",
    "# Hard-code the bearer token\n",
    "bearer_token = 'AAAAAAAAAAAAAAAAAAAAANE9twEAAAAAbj6SVx%2FKE1hExDTy3me2W8pPmmc%3D7xQvh90geD9eWnPN5pBNLShnMq0Vieyxur3v6ARPNe4elqj9ZZ'\n",
    "\n",
    "# Define the user ID\n",
    "user_id = \"14773334\"\n",
    "\n",
    "# Define the endpoint\n",
    "url = f\"https://api.twitter.com/2/users/{user_id}/tweets\"\n",
    "\n",
    "# Calculate the start and end times for the past six months\n",
    "end_time = datetime.utcnow()\n",
    "start_time = end_time - timedelta(days=365)\n",
    "\n",
    "# Format the dates in RFC3339 format with milliseconds\n",
    "end_time_str = end_time.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'\n",
    "start_time_str = start_time.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'\n",
    "\n",
    "# Parameters for the initial request\n",
    "params = {\n",
    "    'max_results': 100,\n",
    "    'start_time': start_time_str,\n",
    "    'end_time': end_time_str,\n",
    "    'tweet.fields': 'created_at,text',\n",
    "    'expansions': 'author_id',\n",
    "    'user.fields': 'username'\n",
    "}\n",
    "\n",
    "# Define the headers with the bearer token for authentication\n",
    "headers = {\n",
    "    'Authorization': f'Bearer {bearer_token}'\n",
    "}\n",
    "\n",
    "all_tweets = []\n",
    "user_info = {}\n",
    "\n",
    "while True:\n",
    "    # Make the request to the Twitter API\n",
    "    response = requests.get(url, headers=headers, params=params)\n",
    "\n",
    "    # Check for a successful response\n",
    "    if response.status_code == 200:\n",
    "        # Parse the JSON response\n",
    "        tweets = response.json()\n",
    "        all_tweets.extend(tweets.get('data', []))\n",
    "\n",
    "        # Extract user information\n",
    "        if 'includes' in tweets and 'users' in tweets['includes']:\n",
    "            for user in tweets['includes']['users']:\n",
    "                user_info[user['id']] = user['username']\n",
    "\n",
    "        # Check if there is a next_token for pagination\n",
    "        next_token = tweets.get('meta', {}).get('next_token')\n",
    "        if next_token:\n",
    "            params['pagination_token'] = next_token\n",
    "        else:\n",
    "            break  # No more pages left to fetch\n",
    "    else:\n",
    "        print(f\"Failed to retrieve tweets: {response.status_code}\")\n",
    "        print(response.text)\n",
    "        break\n",
    "\n",
    "# Merge tweet data with user info\n",
    "for tweet in all_tweets:\n",
    "    tweet['username'] = user_info.get(tweet['author_id'], 'Unknown')\n",
    "\n",
    "# Convert the list of tweets to a DataFrame\n",
    "new_df = pd.DataFrame(all_tweets)\n",
    "\n",
    "# Define the path for the XLSX file\n",
    "file_path = '/Users/dwijesh/Desktop/ProjectFiles/omega2.xlsx'\n",
    "\n",
    "# Check if the file already exists\n",
    "if os.path.exists(file_path):\n",
    "    # Read the existing data\n",
    "    existing_df = pd.read_excel(file_path)\n",
    "    # Append the new data to the existing data\n",
    "    combined_df = pd.concat([existing_df, new_df], ignore_index=True)\n",
    "else:\n",
    "    # If the file doesn't exist, use the new data as the combined data\n",
    "    combined_df = new_df\n",
    "\n",
    "# Save the combined DataFrame to an XLSX file\n",
    "combined_df.to_excel(file_path, index=False)\n",
    "\n",
    "if response.status_code == 200:\n",
    "    print(f\"Tweets saved to {file_path}\")\n",
    "else:\n",
    "    print(response)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "8b5f072f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Cleaned file saved to /Users/dwijesh/Desktop/ProjectFiles/omega2_cleaned.xlsx\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import re\n",
    "import emoji\n",
    "\n",
    "def clean_text(text):\n",
    "    # Remove URLs\n",
    "    text = re.sub(r'http\\S+', '', text)\n",
    "    \n",
    "    # Remove emojis\n",
    "    text = emoji.replace_emoji(text, replace='')\n",
    "    \n",
    "    # Remove @mentions, #hashtags, and other symbols\n",
    "    text = re.sub(r'[@#]\\w+', '', text)\n",
    "    \n",
    "    # Remove non-alphanumeric characters except spaces\n",
    "    text = re.sub(r'[^A-Za-z0-9\\s]', '', text)\n",
    "    \n",
    "    # Remove \"RT\"\n",
    "    text = re.sub(r'\\bRT\\b', '', text)\n",
    "    \n",
    "    return text.strip()\n",
    "\n",
    "# Load the Excel file\n",
    "file_path = '/Users/dwijesh/Desktop/ProjectFiles/omega2.xlsx'\n",
    "data_df = pd.read_excel(file_path, engine='openpyxl')\n",
    "\n",
    "# Remove the 'edit_history_tweet_ids' and 'id' columns\n",
    "columns_to_remove = ['edit_history_tweet_ids', 'id']\n",
    "data_df = data_df.drop(columns=[col for col in columns_to_remove if col in data_df.columns])\n",
    "\n",
    "# Keep only the first 10 characters in the 'created_at' column\n",
    "if 'created_at' in data_df.columns:\n",
    "    data_df['created_at'] = data_df['created_at'].astype(str).str[:10]\n",
    "\n",
    "# Clean the text data in the 'text' column\n",
    "if 'text' in data_df.columns:\n",
    "    data_df['text'] = data_df['text'].apply(clean_text)\n",
    "\n",
    "# Save the modified DataFrame back to the Excel file\n",
    "output_path = '/Users/dwijesh/Desktop/ProjectFiles/omega2_cleaned.xlsx'\n",
    "data_df.to_excel(output_path, index=False)\n",
    "\n",
    "print(f\"Cleaned file saved to {output_path}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "71359b4e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The cleaned DataFrame has been saved to: /Users/dwijesh/Desktop/ProjectFiles/omega2_cleaned_no_empty_rows.xlsx\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "# Load the cleaned Excel file\n",
    "cleaned_file_path = '/Users/dwijesh/Desktop/ProjectFiles/omega2_cleaned.xlsx'\n",
    "cleaned_df = pd.read_excel(cleaned_file_path, engine='openpyxl')\n",
    "\n",
    "# Check for empty rows (if you still want to display them)\n",
    "empty_rows = cleaned_df[cleaned_df.isnull().any(axis=1)]\n",
    "\n",
    "# Drop the empty rows\n",
    "cleaned_df = cleaned_df.dropna()\n",
    "\n",
    "# Save the cleaned DataFrame back to an Excel file\n",
    "output_file_path = '/Users/dwijesh/Desktop/ProjectFiles/omega2_cleaned_no_empty_rows.xlsx'\n",
    "cleaned_df.to_excel(output_file_path, index=False)\n",
    "print(f\"The cleaned DataFrame has been saved to: {output_file_path}\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.11.5"
  },
  "varInspector": {
   "cols": {
    "lenName": 16,
    "lenType": 16,
    "lenVar": 40
   },
   "kernels_config": {
    "python": {
     "delete_cmd_postfix": "",
     "delete_cmd_prefix": "del ",
     "library": "var_list.py",
     "varRefreshCmd": "print(var_dic_list())"
    },
    "r": {
     "delete_cmd_postfix": ") ",
     "delete_cmd_prefix": "rm(",
     "library": "var_list.r",
     "varRefreshCmd": "cat(var_dic_list()) "
    }
   },
   "types_to_exclude": [
    "module",
    "function",
    "builtin_function_or_method",
    "instance",
    "_Feature"
   ],
   "window_display": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
