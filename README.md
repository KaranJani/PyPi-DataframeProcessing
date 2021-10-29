# DataframeProcessing

Handles NaN and Standardizes all values in a Dataframe


### Installation
Run below command to install whole package

```pip install DataframeProcessing```


### Prerequisite
pandas,numpy,sklearn must be installed

To install run below commands

```pip install pandas```  
```pip install numpy```  
```pip install sklearn```

### Import
```from DataframeProcessing import Alter```


### Instance
```variable=Alter()``` 

### fill_na
```varriable.fill_na(dataframe, central_tendency='mean')```   
        fill_na method replaces all the NaN values in a Dataframe

        Parameters:

        ->dataframe: pd.Dataframe
        ->central_tendency(optional): mean/median/mode
        
        
### standard_scaling
```varriable.standard_scaling(dataframe)```   

        standard_scaling method standardize all the values by removing the mean and scaling to unit variance

        Parameters:

        ->dataframe: pandas.Dataframe/numpy.ndarray
        """


        
        
