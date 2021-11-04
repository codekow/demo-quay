#!/bin/sh

# fix limited resources
set_master_schedulable(){
  oc patch --type=merge --patch='{"spec":{"mastersSchedulable": true}}' schedulers.config.openshift.io cluster
}


# create quayadmin
set_quayadmin_pass(){
  #REG_URL=$(oc get)
  REG_URL=example-registry-quay-quay-enterprise.apps.z1m5if4p.eastus2.aroapp.io

  curl -vv -X POST -k "https://${REG_URL}/api/v1/user/initialize" \
    --header 'Content-Type: application/json' \
    --data '{ "username": "quayadmin", "password":"quaypass123", "email": "quayadmin@example.com", , "access_token": true}'

}

# run functions
#set_master_schedulable
#set_quayadmin_pass
