import pandas as pd
import numpy as np
import os 
def merge_text_files(inputFolder, outputFile,label):
    # List for storing each file as item (row for dataframe)
    data = []

    # Get all txt files inside Input Folder
    txt_files = [f for f in os.listdir(inputFolder) if f.endswith('txt')]

    for txt_file in txt_files:
        file_path = os.path.join(inputFolder,txt_file)
        try:
            with open(file_path,'r',encoding='utf-8') as f:
                content = f.read().strip()
                if label == True: 
                
                    data.append(
                        {
                            'file_name':txt_file,
                            'content':content,
                            'sentiment':1
                        }
                    )
                else : 
                     data.append(
                        {
                            'file_name':txt_file,
                            'content':content,
                            'sentiment':0
                        }
                    )                   
        except Exception as e:
            print(f"Error reading {txt_file} : {str(e)}")
            continue
    df = pd.DataFrame(data)
    df.to_csv(outputFile,index=False)
    print(f'Dataframe saved to {outputFile}')
    return None


if __name__ == "__main__":
    positive_input = "nlp_hw1_ahmad_hudhud/raw_data/pos"
    positive_output= "nlp_hw1_ahmad_hudhud/processed_data/pos_data.csv"

    negative_input = 'nlp_hw1_ahmad_hudhud/raw_data/neg'
    negative_output = 'nlp_hw1_ahmad_hudhud/processed_data/neg_data.csv'

    merge_text_files(positive_input,positive_output,1)
    merge_text_files(negative_input,negative_output,0)


