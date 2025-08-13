







import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

project_name = 'ml_project'

list_of_files = [ 

    '.github/workflows/.gitkeep',
    'src/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/components/data_ingestion.py',
    f'src/{project_name}/components/data_transformation.py',
    f'src/{project_name}/components/model_trainer.py',
    f'src/{project_name}/components/model_evaluation.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/pipeline/training_pipeline.py',
    f'src/{project_name}/pipeline/prediction_pipeline.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/utils/common.py',
    f'src/{project_name}/config/configuration.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/entity/config_entity.py',
    f'src/{project_name}/constants/__init__.py',
    'config/config.yaml',
    'params.yaml',
    'schema.yaml',
    'main.py',
    'app.py',
    f'src/{project_name}/logger/logger.py',
    f'src/{project_name}/exceptions/exception.py',
    'test/unit_tests/__init__.py',
    'test/integration_tests/__init__.py',
    'init_setup.sh',
    'requirements.txt',
    'requirements_dev.txt',
    'setup.py',
    'experiments/experiment1.ipynb',
    'templates/index.html',

]

for path in list_of_files :

    file_path = Path(path)
    file_dir , file_name = os.path.split(file_path)

    if file_dir != '':
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Created directory: {file_dir}")

    if not (os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):

        with open(file_path, 'w') as f:

            if file_name.endswith('.py'):
                logging.info(f"Created file: {file_path}")
                pass

    else :
        logging.info(f"File already exists: {file_path} and is not empty.") 