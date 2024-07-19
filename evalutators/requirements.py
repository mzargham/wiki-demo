import pandas as pd

## This class is responsible for building and evaluating the requirements for a given article


class Requirements:
    def __init__(self, folder_path="wiki-demo/outputs/Llama_3_(Language_Model)"):
        self.folder_path = folder_path
        self.sections = []
        self.get_outline()

        self.section_labels = [self.label_section(s) for s in self.sections]
        self.section_requirements = [self.get_section_requirements(sl) for sl in self.section_labels]

    def get_outline(self):
        # Read the outline from the file
        with open(f"{self.folder_path}/storm_gen_article_polished.txt", "r") as file:
            text = file.read()
            outline, sections = self.identify_sections(text, level=1)
            self.sections = sections

        return outline
    
    def identify_sections(text, level=1):
        # Identify the sections
        sections = text.split("\n"+level*"#")
        names = [section.split("\n")[0] for section in sections]
        return names, sections

    def label_section(self, section):

        # get section types from section types csv
        stdf = pd.read_csv("requirements_data/section_types.csv")

        # TODO: rewriet the below to use the stdf instead of the section_keywords
        section_keywords = {
            "Lead section": ["Introduction", "Overview", "Summary"],
            "Body sections": ["Background", "Development", "Architecture", "Timeline", "Features", "Collaborations", "Model Structure", "Training Data", "Algorithms", "Techniques"],
            "Infobox": ["Infobox"],
            "References": ["References", "Citations"],
            "See also": ["See also", "Related Articles"],
            "Further reading": ["Further reading"],
            "External links": ["External links"],
            "Categories": ["Categories"],
            "Notes": ["Notes", "Footnotes"]
        }
        def get_section_type(section):
            for section_type, keywords in section_keywords.items():
                if any(keyword.lower() in section.lower() for keyword in keywords):
                    return section_type
            return "Body sections" # Default to body sections if no match is found
    
        return get_section_type(section)
    
    def get_section_requirements(self, section_label):
        # read requirement by section type csv
        rbsdf = pd.read_csv("requirements_data/requirements_by_section.csv")
        rdf = pd.read_csv("requirements_data/section_level_requirements.csv")

        # Join the dataframes on "name" ~ "requirement name"
        joined_df = pd.merge(rbsdf, rdf, left_on="requirement_name", right_on="name")

        # Drop the redundant 'name' column from rdf
        joined_df = joined_df.drop(columns=["name"]).set_index("requirement_name").T

        # add a new column called "requirements_list" that contains an empty list
        #joined_df["requirements_list"] = [[] for _ in range(len(joined_df))]

        cols = joined_df.columns
        criteria = joined_df.iloc[-1]

        def get_requirements_list(requirement_name):
            requirements_list = []
            for col in cols:
                if joined_df.loc[requirement_name][col] == 1:
                    requirements_list.append(col)
            return requirements_list
        
        return get_requirements_list(section_label)
    
    def evaluate_requirements(self):
        pass

        

        
        
        
            
