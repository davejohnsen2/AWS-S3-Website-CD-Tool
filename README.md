# AWS S3 Website CD Tool

## General
    This Python script is a continuous deployment tool used to update websites on 
    AWS S3 and view the updates in google chrome. It is designed to run in the
    background as the user makes updates to their files. The script polls the last
    modified date of each html and js file in a user defined folder (along with
    sub-folders). When the user saves a change to a file, the script uploads the
    files to a user specified AWS S3 bucket and then opens the updated webpage
    in google chrome.

    Note: Currently you may have to clear the cache to see the updated page (see
    empty cache and hard reload).

    Note: Only tested with Windows OS. 

## Requires
  * [AWS CLI](https://aws.amazon.com/cli) with appropriate credentials to access S3 buckects
  * [Python](https://www.python.org) 

## Inputs
    sitebaseurl: String, Base site URL
        Example:
            sitebaseurl = "https://EXAMPLE.com" 

    bucketls: Dictionary, File types to poll and a corresponding bucket and subfolder
              for uploading changed files of this type
        Example:
            bucketls = {".js": 'MYBUCKET/MYSUBFOLDERFORJSFILES',
            '.html':'MYBUCKET/MYSUBFOLDERFORHTMLFILES'} 

    openchrome: Boolean, True to open updated file in chrome
        Example:
            openchrome = True 

## Example Use Case
    Website updates beyond local environment when it is desirable to see actual
    public facing dev environment. Making incremental updates to prod website with
    immediate verification allowing for quick rollback if needed.     
