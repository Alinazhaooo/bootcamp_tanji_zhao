## Data Storage

### Folder Structure
- `data/raw/`: Stores raw input data as originally downloaded. No modifications are applied here.  
- `data/processed/`: Stores cleaned and transformed datasets, ready for analysis or modeling.  

### Formats Used
- **CSV**: Human-readable and portable, useful for inspection and debugging.  
- **Parquet**: Columnar storage format, efficient for large datasets (smaller size, faster I/O, preserves dtypes).  
- Both formats are maintained to balance ease of use (CSV) and performance (Parquet).  

## Env Usage
- **DATA_DIR**: Base path for all data files  
  - Default: `data/` (if not set) 
- Code will read/write files relative to this variable
  
## Validation Summary
- Checks performed on reload:
  - Shape equality
  - Column consistency (`date`, `price`)
  - Dtype validation:  
    - `date` → datetime  
    - `price` → numeric  
- Assumptions:
  - Input files include `date` and `price`
  - CSV needs `parse_dates=['date']`
  - Parquet preserves dtypes automatically
