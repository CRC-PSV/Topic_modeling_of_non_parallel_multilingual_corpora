# -*- coding: utf-8 -*-
"""
Spyder Editor
Created on Sun Mar 21 14:04:23 2021
@author: Francis Lareau
This is Projectjstor.
Topic model with LDA (Gibbs sampling)
"""

#==============================================================================
# ############################################################## Import library
#==============================================================================

import os
import pandas as pd
import pickle
import lda
import bz2

#==============================================================================
# #################################################### Initialize project paths
#==============================================================================

main_path = os.path.join("D:\projetjstor\Consolidation\Translation")
os.chdir(main_path)

#==============================================================================
# ################################################################# Import data
#==============================================================================

DTM = pd.read_pickle(bz2.BZ2File(
        os.path.join(main_path,
                     "0. Data",
                     "DTM_philosophy_of_science_all.pbz2"), 'rb'))

#==============================================================================
# ################################################################# Compute LDA
#==============================================================================

ldamodel_lda = lda.LDA(n_topics=25, 
                       n_iter=1000,
                       random_state=1234, # random_state=1234
                       alpha=0.4, 
                       eta=0.01)

ldamodel_lda.fit(DTM)

#==============================================================================
# ################################################################ Save results
#==============================================================================

with open(os.path.join(main_path,
                       "0. Data",
                       "LDA_model_philosophy_of_science_all_K25.pkl"), "wb") as f:
    pickle.dump(ldamodel_lda, f, pickle.HIGHEST_PROTOCOL)
    