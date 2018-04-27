import msg
import os

nuPDG = {
  '1000' :  '14',
  '1100' :  '14',
  '1200' : '-14',
  '1300' : '-14',
  '2010' :  '14'}
  
targetPDG = { 
  '1000' : '1000000010',
  '1100' : '1000010010',
  '1200' : '1000000010',
  '1300' : '1000010010',
  '2010' : '1000060120'}

mcseed = "210921029"
nEvents = "100000"
energy = "0.1,120.0"  
generatorList = "Default"
flux = "1/x"

releaselabel = "trunk:default:numu_freenuc"

comparisons = { 
# numu CC inclusive 
   'cmp_numuCC_all' :    { 'datafiles' : ['numuCC_all.xml' ],
		           'dataclass' : 'INXSDataSet',
		           'mcpredictions' : ['INXSPredIncl'],
			   'outprefix' : 'c01c01_'  
		         },
   'cmp_numuCC_lowE' :   { 'datafiles' : ['numuCC_lowE.xml'],
                           'dataclass' : 'INXSDataSet',
			   'mcpredictions' : ['INXSPredIncl'],
			   'outprefix' : 'c01c02_'
			 },
   'cmp_numuCC_highE' :   { 'datafiles' : ['numuCC_highE.xml'],
                           'dataclass' : 'INXSDataSet',
			   'mcpredictions' : ['INXSPredIncl'],
			   'outprefix' : 'c01c03_'
			 },
   'cmp_numuCC_ANL_12FT,2' :   { 'datafiles' : ['numuCC_ANL_12FT,2.xml'],
                                 'dataclass' : 'INXSDataSet',
			         'mcpredictions' : ['INXSPredIncl'],
			         'outprefix' : 'c01d01_'
			       },
   'cmp_numuCC_ANL_12FT,4' :   { 'datafiles' : ['numuCC_ANL_12FT,4.xml'],
                                 'dataclass' : 'INXSDataSet',
			         'mcpredictions' : ['INXSPredIncl'],
			         'outprefix' : 'c01d02_'
			       },
   'cmp_numuCC_BEBC,0' :   { 'datafiles' : ['numuCC_BEBC,0.xml'],
                             'dataclass' : 'INXSDataSet',
			     'mcpredictions' : ['INXSPredIncl'],
			     'outprefix' : 'c01d03_'
			   },
   'cmp_numuCC_BEBC,2' :   { 'datafiles' : ['numuCC_BEBC,2.xml'],
                             'dataclass' : 'INXSDataSet',
			     'mcpredictions' : ['INXSPredIncl'],
			     'outprefix' : 'c01d04_'
			   },
   'cmp_numuCC_BEBC,5' :   { 'datafiles' : ['numuCC_BEBC,5.xml'],
                             'dataclass' : 'INXSDataSet',
			     'mcpredictions' : ['INXSPredIncl'],
			     'outprefix' : 'c01d05_'
			   },
   'cmp_numuCC_BEBC,8' :   { 'datafiles' : ['numuCC_BEBC,8.xml'],
                             'dataclass' : 'INXSDataSet',
			     'mcpredictions' : ['INXSPredIncl'],
			     'outprefix' : 'c01d06_'
			   },
   'cmp_numuCC_BNL_7FT,0' :   { 'datafiles' : ['numuCC_BNL_7FT,0.xml'], 
                                'dataclass' : 'INXSDataSet',
			        'mcpredictions' : ['INXSPredIncl'],
			        'outprefix' : 'c01d07_'
			      },
   'cmp_numuCC_BNL_7FT,4' :   { 'datafiles' : ['numuCC_BNL_7FT,4.xml'],
                                'dataclass' : 'INXSDataSet',
			        'mcpredictions' : ['INXSPredIncl'],
			        'outprefix' : 'c01d08_'
			      },
   'cmp_numuCC_CCFR,2' :   { 'datafiles' : ['numuCC_CCFR,2.xml'],
                             'dataclass' : 'INXSDataSet',
			     'mcpredictions' : ['INXSPredIncl'],
			     'outprefix' : 'c01d09_'
			   },
   'cmp_numuCC_CCFRR,0' :   { 'datafiles' : ['numuCC_CCFRR,0.xml'],
                              'dataclass' : 'INXSDataSet',
			      'mcpredictions' : ['INXSPredIncl'],
			      'outprefix' : 'c01d10_'
			    },
   'cmp_numuCC_CHARM,0' :   { 'datafiles' : ['numuCC_CHARM,0.xml'],
                              'dataclass' : 'INXSDataSet',
			      'mcpredictions' : ['INXSPredIncl'],
			      'outprefix' : 'c01d11_'
			    },
   'cmp_numuCC_CHARM,4' :   { 'datafiles' : ['numuCC_CHARM,4.xml'],
                              'dataclass' : 'INXSDataSet',
			      'mcpredictions' : ['INXSPredIncl'],
			      'outprefix' : 'c01d12_'
			    },
   'cmp_numuCC_FNAL_15FT,1' :   { 'datafiles' : ['numuCC_FNAL_15FT,1.xml'],
                                  'dataclass' : 'INXSDataSet',
			          'mcpredictions' : ['INXSPredIncl'],
			          'outprefix' : 'c01d13_'
			        },
   'cmp_numuCC_FNAL_15FT,2' :   { 'datafiles' : ['numuCC_FNAL_15FT,2.xml'],
                                  'dataclass' : 'INXSDataSet',
			          'mcpredictions' : ['INXSPredIncl'],
			          'outprefix' : 'c01d14_'
			        },
   'cmp_numuCC_Gargamelle,0' :   { 'datafiles' : ['numuCC_Gargamelle,0.xml'],
                                   'dataclass' : 'INXSDataSet',
			           'mcpredictions' : ['INXSPredIncl'],
			           'outprefix' : 'c01d15_'
			         },
   'cmp_numuCC_Gargamelle,10' :   { 'datafiles' : ['numuCC_Gargamelle,10.xml'],
                                    'dataclass' : 'INXSDataSet',
			            'mcpredictions' : ['INXSPredIncl'],
			            'outprefix' : 'c01d16_'
			          },
   'cmp_numuCC_Gargamelle,12' :   { 'datafiles' : ['numuCC_Gargamelle,12.xml'], 
                                    'dataclass' : 'INXSDataSet',
			            'mcpredictions' : ['INXSPredIncl'],
			            'outprefix' : 'c01d17_'
			          },
   'cmp_numuCC_IHEP_ITEP,0' :   { 'datafiles' : ['numuCC_IHEP_ITEP,0.xml'],
                                  'dataclass' : 'INXSDataSet',
			          'mcpredictions' : ['INXSPredIncl'],
			          'outprefix' : 'c01d18_'
			         },
   'cmp_numuCC_IHEP_ITEP,2' :   { 'datafiles' : ['numuCC_IHEP_ITEP,2.xml'],
                                  'dataclass' : 'INXSDataSet',
			          'mcpredictions' : ['INXSPredIncl'],
			          'outprefix' : 'c01d19_'
			         },
   'cmp_numuCC_IHEP_JINR,0' :   { 'datafiles' : ['numuCC_IHEP_JINR,0.xml'],
                                  'dataclass' : 'INXSDataSet',
			          'mcpredictions' : ['INXSPredIncl'],
			          'outprefix' : 'c01d20_'
			         },
   'cmp_numuCC_SKAT,0' :   { 'datafiles' : ['numuCC_SKAT,0.xml'],
                             'dataclass' : 'INXSDataSet',
			     'mcpredictions' : ['INXSPredIncl'],
			     'outprefix' : 'c01d21_'
			   },
   'cmp_numuCC_MINOS,0' :   { 'datafiles' : ['numuCC_MINOS,0.xml'],
                              'dataclass' : 'INXSDataSet',
			      'mcpredictions' : ['INXSPredIncl'],
			      'outprefix' : 'c01d22_'
			    },
   'cmp_numuCC_SciBooNE,0' :   { 'datafiles' : ['numuCC_SciBooNE,0.xml'], 
                                 'dataclass' : 'INXSDataSet',
			         'mcpredictions' : ['INXSPredIncl'],
			         'outprefix' : 'c01d23_'
			       },
# numu CC QE 
   'cmp_numuCCQE_all' :   { 'datafiles' : ['numuCCQE_all.xml'], 
                                 'dataclass' : 'INXSDataSet',
			         'mcpredictions' : ['INXSPredQE'],
			         'outprefix' : 'c03c01_'
			  },
   'cmp_numuCCQE_C12nocorr' :   { 'datafiles' : ['numuCCQE_C12nocorr.xml'],
                                  'dataclass' : 'INXSDataSet',
			          'mcpredictions' : ['INXSPredQE'],
			          'outprefix' : 'c03c02_'
			        },

   'cmp_numuCCQE_ANL_12FT,1' :   { 'datafiles' : ['numuCCQE_ANL_12FT,1.xml'],
                                   'dataclass' : 'INXSDataSet',
			           'mcpredictions' : ['INXSPredQE'],
			           'outprefix' : 'c03d01_'
			         },
   'cmp_numuCCQE_ANL_12FT,3' :   { 'datafiles' : ['numuCCQE_ANL_12FT,3.xml'],
                                   'dataclass' : 'INXSDataSet',
			           'mcpredictions' : ['INXSPredQE'],
			           'outprefix' : 'c03d02_'
			         },
   'cmp_numuCCQE_BEBC,12' :   { 'datafiles' : ['numuCCQE_BEBC,12.xml'],
                                'dataclass' : 'INXSDataSet',
			        'mcpredictions' : ['INXSPredQE'],
			        'outprefix' : 'c03d03_'
			      },
   'cmp_numuCCQE_BNL_7FT,3' :   { 'datafiles' : ['numuCCQE_BNL_7FT,3.xml'],
                                  'dataclass' : 'INXSDataSet',
			          'mcpredictions' : ['INXSPredQE'],
			          'outprefix' : 'c03d04_'
			        },
   'cmp_numuCCQE_FNAL_15FT,3' :   { 'datafiles' : ['numuCCQE_FNAL_15FT,3.xml'],
                                    'dataclass' : 'INXSDataSet',
			            'mcpredictions' : ['INXSPredQE'],
			            'outprefix' : 'c03d05_'
			          },
   'cmp_numuCCQE_Gargamelle,2' :   { 'datafiles' : ['numuCCQE_Gargamelle,2.xml'],
                                     'dataclass' : 'INXSDataSet',
			             'mcpredictions' : ['INXSPredQE'],
			             'outprefix' : 'c03d06_'
			           },
   'cmp_numuCCQE_SERP_A1,0' :   { 'datafiles' : ['numuCCQE_SERP_A1,0.xml'],
                                  'dataclass' : 'INXSDataSet',
			          'mcpredictions' : ['INXSPredQE'],
			          'outprefix' : 'c03d07_'
			        },
   'cmp_numuCCQE_SERP_A1,1' :   { 'datafiles' : ['numuCCQE_SERP_A1,1.xml'], 
                                  'dataclass' : 'INXSDataSet',
			          'mcpredictions' : ['INXSPredQE'],
			          'outprefix' : 'c03d08_'
			        },
   'cmp_numuCCQE_SKAT,8' :   { 'datafiles' : ['numuCCQE_SKAT,8.xml'],
                               'dataclass' : 'INXSDataSet',
			       'mcpredictions' : ['INXSPredQE'],
			       'outprefix' : 'c03d09_'
			     },
   'cmp_numuCCQE_NOMAD,2' :   { 'datafiles' : ['numuCCQE_NOMAD,2.xml'],
                                'dataclass' : 'INXSDataSet',
			        'mcpredictions' : ['INXSPredQE'],
			        'outprefix' : 'c03d10_'
			      },
   'cmp_numuCCQE_NOMAD,0' :   { 'datafiles' : ['numuCCQE_NOMAD,0.xml'],
                                'dataclass' : 'INXSDataSet',
			        'mcpredictions' : ['INXSPredQE'],
			        'outprefix' : 'c03d11_'
			      },
   'cmp_numuCCQE_MiniBooNE,0' :   { 'datafiles' : ['numuCCQE_MiniBooNE,0.xml'],
                                    'dataclass' : 'INXSDataSet',
			            'mcpredictions' : ['INXSPredQE'],
			            'outprefix' : 'c03d12_'
			          },
   'cmp_numuCCQE_LSND,0' :   { 'datafiles' : ['numuCCQE_LSND,0.xml'], 
                               'dataclass' : 'INXSDataSet',
			       'mcpredictions' : ['INXSPredQE'],
			       'outprefix' : 'c03d10_'
			     },
# numu CC 1pi 
   'cmp_numuCCppi+_all' :   { 'datafiles' : ['numuCCppi+_all.xml'], 
                              'dataclass' : 'INXSDataSet',
			      'mcpredictions' : ['INXSPredExclPion'],
			      'outprefix' : 'c05c01_'
			    },
   'cmp_numuCCppi+_ANL_12FT,0' :   { 'datafiles' : ['numuCCppi+_ANL_12FT,0.xml'],
                                     'dataclass' : 'INXSDataSet',
			             'mcpredictions' : ['INXSPredExclPion'],
			             'outprefix' : 'c05d01_'
			           },
   'cmp_numuCCppi+_ANL_12FT,5' :   { 'datafiles' : ['numuCCppi+_ANL_12FT,5.xml'],
                                     'dataclass' : 'INXSDataSet',
			             'mcpredictions' : ['INXSPredExclPion'],
			             'outprefix' : 'c05d02_'
			           },
   'cmp_numuCCppi+_ANL_12FT,8' :   { 'datafiles' : ['numuCCppi+_ANL_12FT,8.xml'],
                                     'dataclass' : 'INXSDataSet',
			             'mcpredictions' : ['INXSPredExclPion'],
			             'outprefix' : 'c05d03_'
			           },
   'cmp_numuCCppi+_BEBC,4' :   { 'datafiles' : ['numuCCppi+_BEBC,4.xml'],
                                 'dataclass' : 'INXSDataSet',
			         'mcpredictions' : ['INXSPredExclPion'],
			         'outprefix' : 'c05d04_'
			       },
   'cmp_numuCCppi+_BEBC,9' :   { 'datafiles' : ['numuCCppi+_BEBC,9.xml'],
                                 'dataclass' : 'INXSDataSet',
			         'mcpredictions' : ['INXSPredExclPion'],
			         'outprefix' : 'c05d05_'
			       },
   'cmp_numuCCppi+_BEBC,13' :   { 'datafiles' : ['numuCCppi+_BEBC,13.xml'],
                                  'dataclass' : 'INXSDataSet',
			          'mcpredictions' : ['INXSPredExclPion'],
			          'outprefix' : 'c05d06_'
			        },
   'cmp_numuCCppi+_BNL_7FT,5' :   { 'datafiles' : ['numuCCppi+_BNL_7FT,5.xml'],
                                    'dataclass' : 'INXSDataSet',
			            'mcpredictions' : ['INXSPredExclPion'],
			            'outprefix' : 'c05d07_'
			          },
   'cmp_numuCCppi+_FNAL_15FT,0' :   { 'datafiles' : ['numuCCppi+_FNAL_15FT,0.xml'],
                                      'dataclass' : 'INXSDataSet',
			              'mcpredictions' : ['INXSPredExclPion'],
			              'outprefix' : 'c05d08_'
			            },
   'cmp_numuCCppi+_Gargamelle,4' :   { 'datafiles' : ['numuCCppi+_Gargamelle,4.xml'], 
                                       'dataclass' : 'INXSDataSet',
			               'mcpredictions' : ['INXSPredExclPion'],
			               'outprefix' : 'c05d09_'
			             },
   'cmp_numuCCppi+_SKAT,4' :   { 'datafiles' : ['numuCCppi+_SKAT,4.xml'],
                                 'dataclass' : 'INXSDataSet',
			         'mcpredictions' : ['INXSPredExclPion'],
			         'outprefix' : 'c05d10_'
			       },
   'cmp_numuCCppi+_SKAT,5' :   { 'datafiles' : ['numuCCppi+_SKAT,5.xml'], 
                                 'dataclass' : 'INXSDataSet',
			         'mcpredictions' : ['INXSPredExclPion'],
			         'outprefix' : 'c05d11_'
			       },
   'cmp_numuCCnpi+_all' :   { 'datafiles' : ['numuCCnpi+_all.xml'], 
                              'dataclass' : 'INXSDataSet',
			      'mcpredictions' : ['INXSPredExclPion'],
			      'outprefix' : 'c06c01_'
			    },
   'cmp_numuCCnpi+_ANL_12FT,7' :   { 'datafiles' : ['numuCCnpi+_ANL_12FT,7.xml'],
                                     'dataclass' : 'INXSDataSet',
			             'mcpredictions' : ['INXSPredExclPion'],
			             'outprefix' : 'c06d01_'
			           },
   'cmp_numuCCnpi+_ANL_12FT,10' :   { 'datafiles' : ['numuCCnpi+_ANL_12FT,10.xml'],
                                      'dataclass' : 'INXSDataSet',
			              'mcpredictions' : ['INXSPredExclPion'],
			              'outprefix' : 'c06d02_'
			            },
   'cmp_numuCCnpi+_BNL_7FT,7' :   { 'datafiles' : ['numuCCnpi+_BNL_7FT,7.xml'],
                                    'dataclass' : 'INXSDataSet',
			            'mcpredictions' : ['INXSPredExclPion'],
			            'outprefix' : 'c06d03_'
			          },
   'cmp_numuCCnpi+_SKAT,7' :   { 'datafiles' : ['numuCCnpi+_SKAT,7.xml'], 
                                 'dataclass' : 'INXSDataSet',
			         'mcpredictions' : ['INXSPredExclPion'],
			         'outprefix' : 'c06d04_'
			       },
   'cmp_numuCCppi0_all' :   { 'datafiles' : ['numuCCppi0_all.xml'], 
                              'dataclass' : 'INXSDataSet',
			      'mcpredictions' : ['INXSPredExclPion'],
			      'outprefix' : 'c07c01_'
			    },
   'cmp_numuCCppi0_ANL_12FT,6' :   { 'datafiles' : ['numuCCppi0_ANL_12FT,6.xml'],
                                     'dataclass' : 'INXSDataSet',
			             'mcpredictions' : ['INXSPredExclPion'],
			             'outprefix' : 'c07d01_'
			           },
   'cmp_numuCCppi0_ANL_12FT,9' :   { 'datafiles' : ['numuCCppi0_ANL_12FT,9.xml'],
                                     'dataclass' : 'INXSDataSet',
			             'mcpredictions' : ['INXSPredExclPion'],
			             'outprefix' : 'c07d02_'
			           },
   'cmp_numuCCppi0_BNL_7FT,6' :   { 'datafiles' : ['numuCCppi0_BNL_7FT,6.xml'],
                                    'dataclass' : 'INXSDataSet',
			            'mcpredictions' : ['INXSPredExclPion'],
			            'outprefix' : 'c07d03_'
			          },
   'cmp_numuCCppi0_SKAT,6' :   { 'datafiles' : ['numuCCppi0_SKAT,6.xml'], 
                                 'dataclass' : 'INXSDataSet',
			         'mcpredictions' : ['INXSPredExclPion'],
			         'outprefix' : 'c07d04_'
			       },
# numu CC 2pi
   'cmp_numuCCn2pi+_all' :   { 'datafiles' : ['numuCCn2pi+_all.xml'], 
                               'dataclass' : 'INXSDataSet',
			       'mcpredictions' : ['INXSPredExclPion'],
			       'outprefix' : 'c08c01_'
			     },
   'cmp_numuCCn2pi+_ANL_12FT,13' :   { 'datafiles' : ['numuCCn2pi+_ANL_12FT,13.xml'], 
                                       'dataclass' : 'INXSDataSet',
			               'mcpredictions' : ['INXSPredExclPion'],
			               'outprefix' : 'c08d01_'
			             },
   'cmp_numuCCppi+pi0_all' :   { 'datafiles' : ['numuCCppi+pi0_all.xml'], 
                                  'dataclass' : 'INXSDataSet',
			          'mcpredictions' : ['INXSPredExclPion'],
			          'outprefix' : 'c09c01_'
			        },
   'cmp_numuCCppi+pi0_ANL_12FT,12' :   { 'datafiles' : ['numuCCppi+pi0_ANL_12FT,12.xml'], 
                                         'dataclass' : 'INXSDataSet',
			                 'mcpredictions' : ['INXSPredExclPion'],
			                 'outprefix' : 'c09d01_'
			               },
   'cmp_numuCCppi+pi-_all' :   { 'datafiles' : ['numuCCppi+pi-_all.xml'], 
                                  'dataclass' : 'INXSDataSet',
			          'mcpredictions' : ['INXSPredExclPion'],
			          'outprefix' : 'c10c01_'
			        },
   'cmp_numuCCppi+pi-_ANL_12FT,11' :   { 'datafiles' : ['numuCCppi+pi-_ANL_12FT,11.xml'], 
                                         'dataclass' : 'INXSDataSet',
			                 'mcpredictions' : ['INXSPredExclPion'],
			                 'outprefix' : 'c10d01_'
			               },
   'cmp_numuCCppi+pi-_BNL_7FT,8' :   { 'datafiles' : ['numuCCppi+pi-_BNL_7FT,8.xml'],  
                                       'dataclass' : 'INXSDataSet',
			               'mcpredictions' : ['INXSPredExclPion'],
			               'outprefix' : 'c10d02_'
			             },
#
# PROBLEMATIC - all bail out with the "not in the new framework" error message
#
# numu coherent pi
#   'cmp_numuNCcohpi0_Ne20' :   { 'datafiles' : ['numuNCcohpi0_Ne20.xml'],  # problematic - not in the new fwk
#                                       'dataclass' : 'INXSDataSet',
#			               'mcpredictions' : ['INXSPredPrecompCohPion'],
#			               'outprefix' : 'c11c01_'
#			             },
#   'cmp_numuNCcohpi0_Al27' :   { 'datafiles' : ['numuNCcohpi0_Al27.xml'],  # problematic - not in the new fwk
#                                       'dataclass' : 'INXSDataSet',
#			               'mcpredictions' : ['INXSPredPrecompCohPion'],
#			               'outprefix' : 'c11c02_'
#			             },
#   'cmp_numuNCcohpi0_Si30' :   { 'datafiles' : ['numuNCcohpi0_Si30.xml'],  # problematic - not in the new fwk
#                                       'dataclass' : 'INXSDataSet',
#			               'mcpredictions' : ['INXSPredPrecompCohPion'],
#			               'outprefix' : 'c11c03_'
#			             },
#   'cmp_numuCCcohpi+_Ne20' :   { 'datafiles' : ['numuCCcohpi+_Ne20.xml'],  # problematic - not in the new fwk
#                                       'dataclass' : 'INXSDataSet',
#			               'mcpredictions' : ['INXSPredPrecompCohPion'],
#			               'outprefix' : 'c12c01_'
#			             },
#   'cmp_numuCCcohpi+_Si30' :   { 'datafiles' : ['numuCCcohpi+_Si30.xml'],  # problematic - not in the new fwk
#                                       'dataclass' : 'INXSDataSet',
#			               'mcpredictions' : ['INXSPredPrecompCohPion'],
#			               'outprefix' : 'c12c02_'
#			             },
# numubar coherent pi
#   'cmp_numubarCCcohpi-_Ne20' :   { 'datafiles' : ['numubarCCcohpi-_Ne20.xml'],  # problematic - not in the new fwk
#                                       'dataclass' : 'INXSDataSet',
#			               'mcpredictions' : ['INXSPredPrecompCohPion'],
#			               'outprefix' : 'c13c01_'
#			             },
#   'cmp_numubarCCcohpi-_Si30' :   { 'datafiles' : ['numubarCCcohpi-_Si30.xml'],  # problematic - not in the new fwk
#                                       'dataclass' : 'INXSDataSet',
#			               'mcpredictions' : ['INXSPredPrecompCohPion'],
#			               'outprefix' : 'c13c02_'
#			             },
# numubar CC inclusive 
   'cmp_numubarCC_all' : { 'datafiles' : ['numubarCC_all.xml' ], 
		           'dataclass' : 'INXSDataSet',
		           'mcpredictions' : ['INXSPredIncl'],
			   'outprefix' : 'c02c01_'
                         },
   'cmp_numubarCC_lowE' : { 'datafiles' : ['numubarCC_lowE.xml' ],
		            'dataclass' : 'INXSDataSet',
		            'mcpredictions' : ['INXSPredIncl'],
			    'outprefix' : 'c02c02_'
                          },
   'cmp_numubarCC_highE' : { 'datafiles' : ['numubarCC_highE.xml' ],
		             'dataclass' : 'INXSDataSet',
		             'mcpredictions' : ['INXSPredIncl'],
			     'outprefix' : 'c02c03_'
                           },
   'cmp_numubarCC_BEBC,1' :   { 'datafiles' : ['numubarCC_BEBC,1.xml'],
                                'dataclass' : 'INXSDataSet',
			        'mcpredictions' : ['INXSPredIncl'],
			        'outprefix' : 'c02d01_'
			      },
   'cmp_numubarCC_BEBC,3' :   { 'datafiles' : ['numubarCC_BEBC,3.xml'],
                                'dataclass' : 'INXSDataSet',
			        'mcpredictions' : ['INXSPredIncl'],
			        'outprefix' : 'c02d02_'
			      },
   'cmp_numubarCC_BEBC,6' :   { 'datafiles' : ['numubarCC_BEBC,6.xml'],
                                'dataclass' : 'INXSDataSet',
			        'mcpredictions' : ['INXSPredIncl'],
			        'outprefix' : 'c02d03_'
			      },
   'cmp_numubarCC_BEBC,7' :   { 'datafiles' : ['numubarCC_BEBC,7.xml'],
                                'dataclass' : 'INXSDataSet',
			        'mcpredictions' : ['INXSPredIncl'],
			        'outprefix' : 'c02d04_'
			      },
   'cmp_numubarCC_BNL_7FT,1' :   { 'datafiles' : ['numubarCC_BNL_7FT,1.xml'],
                                'dataclass' : 'INXSDataSet',
			        'mcpredictions' : ['INXSPredIncl'],
			        'outprefix' : 'c02d05_'
			      },
   'cmp_numubarCC_CCFR,3' :   { 'datafiles' : ['numubarCC_CCFR,3.xml'],
                                'dataclass' : 'INXSDataSet',
			        'mcpredictions' : ['INXSPredIncl'],
			        'outprefix' : 'c02d06_'
			      },
   'cmp_numubarCC_CHARM,1' :   { 'datafiles' : ['numubarCC_CHARM,1.xml'], 
                                 'dataclass' : 'INXSDataSet',
			         'mcpredictions' : ['INXSPredIncl'],
			         'outprefix' : 'c02d07_'
			       },
   'cmp_numubarCC_CHARM,5' :   { 'datafiles' : ['numubarCC_CHARM,5.xml'],
                                 'dataclass' : 'INXSDataSet',
			         'mcpredictions' : ['INXSPredIncl'],
			         'outprefix' : 'c02d08_'
			       },
   'cmp_numubarCC_FNAL_15FT,4' :   { 'datafiles' : ['numubarCC_FNAL_15FT,4.xml'],
                                     'dataclass' : 'INXSDataSet',
			             'mcpredictions' : ['INXSPredIncl'],
			             'outprefix' : 'c02d09_'
			           },
   'cmp_numubarCC_FNAL_15FT,5' :   { 'datafiles' : ['numubarCC_FNAL_15FT,5.xml'],
                                     'dataclass' : 'INXSDataSet',
			             'mcpredictions' : ['INXSPredIncl'],
			             'outprefix' : 'c02d10_'
			           },
   'cmp_numubarCC_Gargamelle,1' :   { 'datafiles' : ['numubarCC_Gargamelle,1.xml'],
                                      'dataclass' : 'INXSDataSet',
			              'mcpredictions' : ['INXSPredIncl'],
			              'outprefix' : 'c02d11_'
			            },
   'cmp_numubarCC_Gargamelle,11' :   { 'datafiles' : ['numubarCC_Gargamelle,11.xml'],
                                       'dataclass' : 'INXSDataSet',
			               'mcpredictions' : ['INXSPredIncl'],
			               'outprefix' : 'c02d12_'
			             },
   'cmp_numubarCC_Gargamelle,13' :   { 'datafiles' : ['numubarCC_Gargamelle,13.xml'],
                                       'dataclass' : 'INXSDataSet',
			               'mcpredictions' : ['INXSPredIncl'],
			               'outprefix' : 'c02d13_'
			             },
   'cmp_numubarCC_IHEP_ITEP,1' :   { 'datafiles' : ['numubarCC_IHEP_ITEP,1.xml'],
                                     'dataclass' : 'INXSDataSet',
			             'mcpredictions' : ['INXSPredIncl'],
			             'outprefix' : 'c02d14_'
			           },
   'cmp_numubarCC_IHEP_ITEP,3' :   { 'datafiles' : ['numubarCC_IHEP_ITEP,3.xml'],
                                     'dataclass' : 'INXSDataSet',
			             'mcpredictions' : ['INXSPredIncl'],
			             'outprefix' : 'c02d15_'
			           },
   'cmp_numubarCC_IHEP_JINR,1' :   { 'datafiles' : ['numubarCC_IHEP_ITEP,1.xml'],
                                     'dataclass' : 'INXSDataSet',
			             'mcpredictions' : ['INXSPredIncl'],
			             'outprefix' : 'c02d16_'
			           },
   'cmp_numubarCC_MINOS,1' :   { 'datafiles' : ['numubarCC_MINOS,1.xml'], 
                                 'dataclass' : 'INXSDataSet',
			         'mcpredictions' : ['INXSPredIncl'],
			         'outprefix' : 'c02d14_'
			       },
# numubar CC QE 
   'cmp_numubarCCQE_all' :   { 'datafiles' : ['numubarCCQE_all.xml'], 
                               'dataclass' : 'INXSDataSet',
			       'mcpredictions' : ['INXSPredQE'],
			       'outprefix' : 'c04c01_'
			     },
   'cmp_numubarCCQE_BNL_7FT,2' :   { 'datafiles' : ['numubarCCQE_BNL_7FT,2.xml'],
                                     'dataclass' : 'INXSDataSet',
			             'mcpredictions' : ['INXSPredQE'],
			             'outprefix' : 'c04d01_'
			           },
   'cmp_numubarCCQE_Gargamelle,3' :   { 'datafiles' : ['numubarCCQE_Gargamelle,3.xml'],
                                        'dataclass' : 'INXSDataSet',
			                'mcpredictions' : ['INXSPredQE'],
			                'outprefix' : 'c04d02_'
			              },
   'cmp_numubarCCQE_Gargamelle,5' :   { 'datafiles' : ['numubarCCQE_Gargamelle,5.xml'],
                                        'dataclass' : 'INXSDataSet',
			                'mcpredictions' : ['INXSPredQE'],
			                'outprefix' : 'c04d03_'
			              },
   'cmp_numubarCCQE_SERP_A1,2' :   { 'datafiles' : ['numubarCCQE_SERP_A1,2.xml'],
                                     'dataclass' : 'INXSDataSet',
			             'mcpredictions' : ['INXSPredQE'],
			             'outprefix' : 'c04d04_'
			           },
   'cmp_numubarCCQE_SKAT,9' :   { 'datafiles' : ['numubarCCQE_SKAT,9.xml'],
                                  'dataclass' : 'INXSDataSet',
			          'mcpredictions' : ['INXSPredQE'],
			          'outprefix' : 'c04d05_'
			        },
   'cmp_numubarCCQE_NOMAD,3' :   { 'datafiles' : ['numubarCCQE_NOMAD,3.xml'],
                                   'dataclass' : 'INXSDataSet',
			           'mcpredictions' : ['INXSPredQE'],
			           'outprefix' : 'c04d06_'
			         },
   'cmp_numubarCCQE_NOMAD,1' :   { 'datafiles' : ['numubarCCQE_NOMAD,1.xml'], 
                                   'dataclass' : 'INXSDataSet',
			           'mcpredictions' : ['INXSPredQE'],
			           'outprefix' : 'c04d07_'
			         } # *** NOTE *** RESTORE the comma when the time comes to restore problematic ones !
#
# PROBLEMATIC - all bail out with the "not in the new framework" error message
#
# Cross-section ratios
# numubar CC inclusive / numu CC inclusive
#   'cmp_numubarCC_over_numuCC_MINOS,2' :   { 'datafiles' : ['numubarCC_over_numuCC_MINOS,2.xml'], # problematic - not in the new fwk
#                                   'dataclass' : 'INXSDataSet',
#			           'mcpredictions' : ['INXSPredNull'],
#			           'outprefix' : 'c14d01_'
#			         },
# numu CC pi0 / numu CCQE
#   'cmp_numuCCpi0_over_numuCCQE_K2K,0' :   { 'datafiles' : ['numuCCpi0_over_numuCCQE_K2K,0.xml'], # problematic - not in the new fwk
#                                   'dataclass' : 'INXSDataSet',
#			           'mcpredictions' : ['INXSPredNull'],
#			           'outprefix' : 'c15d01_'
#			         },
# Dileptons
#   'cmp_numuCC_dilepton_ratio_worldavg' : { 'datafiles' : ['numuCC_dilepton_ratio_worldavg.xml'], # problematic - not in the new fwk
#                                            'dataclass' : 'INXSDataSet',
#			                    'mcpredictions' : ['INXSPredNull'],
#			                    'outprefix' : 'c16c01_'
#                                          },
#   'cmp_numubarCC_dilepton_ratio_worldavg' : { 'datafiles' : ['numubarCC_dilepton_ratio_worldavg.xml'], # problematic - not in the new fwk
#                                               'dataclass' : 'INXSDataSet',
#			                       'mcpredictions' : ['INXSPredNull'],
#			                       'outprefix' : 'c16c02_'
#                                             },
#   'cmp_numuCC_charm_ratio_worldavg' : { 'datafiles' : ['numuCC_charm_ratio_worldavg.xml'], # problematic - not in the new fwk
#                                         'dataclass' : 'INXSDataSet',
#			                 'mcpredictions' : ['INXSPredNull'],
#			                 'outprefix' : 'c16c03_'
#                                       },
#   'cmp_numuCC_dilepton_cdhs' : { 'datafiles' : ['numuCC_dilepton_cdhs.xml'], # problematic - not in the new fwk
#                                  'dataclass' : 'INXSDataSet',
#			          'mcpredictions' : ['INXSPredNull'],
#			          'outprefix' : 'c16d01_'
#                                },
#   'cmp_numuCC_dilepton_nomad' : { 'datafiles' : ['numuCC_dilepton_nomad.xml'], # problematic - not in the new fwk
#                                   'dataclass' : 'INXSDataSet',
#			           'mcpredictions' : ['INXSPredNull'],
#			           'outprefix' : 'c16d02_'
#                                 },
#   'cmp_numuCC_dilepton_e744_e770' : { 'datafiles' : ['numuCC_dilepton_e744_e770.xml'], # problematic - not in the new fwk
#                                       'dataclass' : 'INXSDataSet',
#			               'mcpredictions' : ['INXSPredNull'],
#			               'outprefix' : 'c16d03_'
#                                     },
#   'cmp_numuCC_dilepton_e744' : { 'datafiles' : ['numuCC_dilepton_e744.xml'], # problematic - not in the new fwk
#                                  'dataclass' : 'INXSDataSet',
#			          'mcpredictions' : ['INXSPredNull'],
#			          'outprefix' : 'c16d04_'
#                                },
#   'cmp_numuCC_dilepton_fnal15ft' : { 'datafiles' : ['numuCC_dilepton_fnal15ft.xml'], # problematic - not in the new fwk
#                                      'dataclass' : 'INXSDataSet',
#			              'mcpredictions' : ['INXSPredNull'],
#			              'outprefix' : 'c16d05_'
#                                    },
#   'cmp_numuCC_dilepton_gargamelle' : { 'datafiles' : ['numuCC_dilepton_gargamelle.xml'], # problematic - not in the new fwk
#                                        'dataclass' : 'INXSDataSet',
#			                'mcpredictions' : ['INXSPredNull'],
#			                'outprefix' : 'c16d06_'
#                                      }
}


def fillDAG (jobsub, tag, date, paths, regretags, regredir ):
  fillDAG_GHEP (jobsub, tag, paths['xsec_A'], paths['xsecval'])
  fillDAG_GST (jobsub, paths['xsecval'])
  createFileList (tag, date, paths['xsec_A'], paths['xsecval'], paths['xseclog'], regretags )
  createCmpConfig (tag, date, paths['xseclog'] ) 
  fillDAG_cmp (jobsub, tag, date, paths['xsec_A'], paths['xsecval'], paths['xseclog'], regretags, regredir ) 

def fillDAG_GHEP (jobsub, tag, xsec_a_path, out):
  # check if job is done already
  if isDoneGHEP (out):
    msg.warning ("xsec validation ghep files found in " + out + " ... " + msg.BOLD + "skipping xsecval:fillDAG_GHEP\n", 1)
    return
  #not done, add jobs to dag
  msg.info ("\tAdding xsec validation (ghep) jobs\n")
  # in parallel mode
  jobsub.add ("<parallel>")
  # common configuration
  inputFile = "gxspl-vA-" + tag + ".xml"
  options   = " -n " + nEvents + " -e " + energy + " -f " + flux + " --seed " + mcseed + \
              " --cross-sections input/" + inputFile + " --event-generator-list " + generatorList
  # loop over keys and generate gevgen command
  for key in nuPDG.iterkeys():
    cmd = "gevgen " + options + " -p " + nuPDG[key] + " -t " + targetPDG[key] + " -r " + key
    logFile = "gevgen_" + key + ".log"
    jobsub.addJob (xsec_a_path + "/" + inputFile, out, logFile, cmd, None)
  # done
  jobsub.add ("</parallel>")

def fillDAG_GST (jobsub, out):
  # check if job is done already
  if isDoneGST (out):
    msg.warning ("xsec validation gst files found in " + out + " ... " + msg.BOLD + "skipping xsecval:fillDAG_GST\n", 1)
    return
  # not done, add jobs to dag
  msg.info ("\tAdding xsec validation (gst) jobs\n")
  # in parallel mode
  jobsub.add ("<parallel>")
  # loop over keys and generate gntpc command
  for key in nuPDG.iterkeys():
    inputFile = "gntp." + key + ".ghep.root"
    logFile = "gntpc" + key + ".log"
    cmd = "gntpc -f gst -i input/" + inputFile
    jobsub.addJob (out + "/" + inputFile, out, logFile, cmd, None)
  # done
  jobsub.add ("</parallel>")

def createFileList (tag, date, xsec_a_path, outEvent, outRep, regretags):
  
  # create xml file with the file list in the format as src/scripts/production/misc/make_genie_sim_file_list.pl
  xmlFile = outRep + "/file_list-" + tag + "-" + date + ".xml"
  try: os.remove (xmlFile)
  except OSError: pass
  xml = open (xmlFile, 'w');
  print >>xml, '<?xml version="1.0" encoding="ISO-8859-1"?>'
  print >>xml, '<genie_simulation_outputs>'
  print >>xml, '\t<model name="' + tag + '-' + date + ':default:world' '">'
  for key in nuPDG.iterkeys():
    print >>xml, '\t\t<evt_file format="ghep"> input/gntp.' + key + '.ghep.root </evt_file>'
  print >>xml, '\t\t<xsec_file> input/xsec-vA-' + tag + '.root </xsec_file>'
  print >>xml, '\t</model>'
  if not (regretags is None):
     for rt in range(len(regretags)):
        rversion, rdate = regretags[rt].split("/") 
	print >>xml, '\t<model name="' + regretags[rt] + ':default:world' '">'
        for key in nuPDG.iterkeys():
           print >>xml, '\t\t<evt_file format="ghep"> input/regre/' +  regretags[rt] +'/gntp.' + key + '.ghep.root </evt_file>'
        print >>xml, '\t\t<xsec_file> input/regre/'  + regretags[rt] + '/xsec-vA-' + rversion + '.root </xsec_file>'
        print >>xml, '\t</model>'
  print >>xml, '</genie_simulation_outputs>'
  xml.close()

def createCmpConfig( tag, date, reportdir ):

   # start GLOBAL CMP CONFIG
   for key in comparisons.iterkeys():
      gcfg = reportdir + "/" + key + "-" + tag + "-" + date + ".xml"
      try: os.remove(gcfg)
      except OSError: pass
      gxml = open( gcfg, 'w' )
      print >>gxml, '<?xml version="1.0" encoding="ISO-8859-1"?>'
      print >>gxml, '<config>'
      print >>gxml, '\t<experiment name="INuXSecWorld">'
      print >>gxml, '\t\t<paths_relative_to_geniecmp_topdir> false </paths_relative_to_geniecmp_topdir>'

      print >>gxml, '\t\t\t<comparison>'

      for i in range( len( comparisons[key]['datafiles'] ) ):
         print >>gxml, '\t\t\t\t<spec>'
         print >>gxml, '\t\t\t\t\t<path2data> data/measurements/vA/intg_xsec/' + comparisons[key]['datafiles'][i] + ' </path2data>'
         print >>gxml, '\t\t\t\t\t<dataclass> ' + comparisons[key]['dataclass'] + ' </dataclass>'
         print >>gxml, '\t\t\t\t\t<predictionclass> ' + comparisons[key]['mcpredictions'][i] + ' </predictionclass>'
         print >>gxml, '\t\t\t\t</spec>'

      gsimfile = "/file_list-" + tag + "-" + date + ".xml"
      print >>gxml, '\t\t\t\t<genie> input' + gsimfile + ' </genie>'
      
      print >>gxml, '\t\t\t</comparison>'
      # now finish up and close global config
      print >>gxml, '\t</experiment>'
      print >>gxml, '</config>'
      gxml.close()
      
#   def fillDAG_cmp (jobsub, tag, date, xsec_a_path, outEvents, outRep, outRepSng):
def fillDAG_cmp (jobsub, tag, date, xsec_a_path, outEvents, outRep, regretags, regredir):
  # check if job is done already
  if isDoneData (tag, date, outRep):
    msg.warning ("xsec validation plots found in " + outRep + " ... " + msg.BOLD + "skipping xsecval:fillDAG_data\n", 1)
    return
  # not done, add jobs to dag
  msg.info ("\tAdding xsec validation (data) jobs\n")    
  inputs = outRep + "/*.xml " + xsec_a_path + "/xsec-vA-" + tag + ".root " + outEvents + "/*.ghep.root"
  # in parallel mode
  jobsub.add ("<parallel>")
  for comp in comparisons:
    inFile = comp + "-" + tag + "-" + date + ".xml"    
    outFile = "genie_" + tag + "_" + comparisons[comp]['outprefix'] + comp 
    cmd = "gvld_general_comparison --no-root-output --global-config input/" + inFile + " -o " + outFile 
    logFile = "gvld_nu_xsec_" + comp + ".log"
    regre = None
    if not (regretags is None):
       regre = ""
       for rt in range(len(regretags)):
          rversion, rdate = regretags[rt].split("/")
	  regre = regre + regredir + "/" + regretags[rt] + "/xsec/nuA/xsec-vA-" + rversion + ".root " 
	  regre = regre + regredir + "/" + regretags[rt] + "/events/xsec_validation/*.ghep.root " 
    jobsub.addJob (inputs, outRep, logFile, cmd, regre)
  # done
  jobsub.add ("</parallel>")

def isDoneGHEP (path):
  # check if given path contains all ghep files
  for key in nuPDG.iterkeys():
    if "gntp." + key + ".ghep.root" not in os.listdir (path): return False
  return True
  
def isDoneGST (path):
  # check if given path contains all gst files
  for key in nuPDG.iterkeys():
    if "gntp." + key + ".gst.root" not in os.listdir (path): return False
  return True
  
def isDoneData (tag, date, path):
  # check if given path contains all plots
  if "genie_" + tag + "-" + date + "-world_nu_xsec_data_comp-all-withref.ps" not in os.listdir (path): return False
  return True
