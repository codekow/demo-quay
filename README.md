# Quay on OCP 4.x Demo

The goal of this repo is to help demonstrate the value of quay and it's integrations.

## QuickStart
```
oc apply -k catalog/openshift-container-storage-operator
oc apply -k catalog/openshift-quay-operator
oc apply -f resources/demo-quay-registry
```

# Links
- [Docs - Deploy Quay on Openshift][1]
- [RH Public Sector Demos][2]

# Integrations
- Sample integration with Microsoft Teams. Quay supports notifications through a variety of providers. e.g., the Clair scanner finds a vulnerability and posts an alert to the security team's channel in MS Teams. Many thanks to [@jilleJr][3] for the code snippet.
```shell
{
    "@type": "MessageCard",
    "@context": "http://schema.org/extensions",
    "themeColor": "d71e00",
    "summary": "Vulnerability detected in ${name}, first tag: ${tags[0]}",
    "sections": [{
        "activityTitle": "Vulnerability Detected",
        "activitySubtitle": "In repository ${name}",
        "activityImage": "https://github.com/quay/quay/raw/master/static/img/quay-icon-stripe.png",
        "facts": [{
            "name": "Repository",
            "value": "${repository}"
        }, {
            "name": "First 5 tags",
            "value": "${tags[0]}, ${tags[1]}, ${tags[2]}, ${tags[3]}, ${tags[4]}"
        }, {
            "name": "Vulnerability ID",
            "value": "${vulnerability.id}"
        }, {
            "name": "Priority",
            "value": "${vulnerability.priority}"
        }, {
            "name": "Description",
            "value": "${vulnerability.description}"
        }, {
            "name": "Has fix?",
            "value": "${vulnerability.has_fix}"
        }],
        "markdown": false
    }],
    "potentialAction": [{
        "@type": "OpenUri",
        "name": "Show Quay.io repository",
        "targets": [{
            "os": "default",
            "uri": "${homepage}"
        }]
      }, {
        "@type": "OpenUri",
        "name": "Show ${vulnerability.id}",
        "targets": [{
            "os": "default",
            "uri": "${vulnerability.link}"
        }]
    }]
}
```


# Links (Red Hat - Internal)
- [RHU - Quay Training][4]
- [ARO RHPDS Lab Guide][5]

[1]:	https://access.redhat.com/documentation/en-us/red_hat_quay/3.6/html/deploy_red_hat_quay_on_openshift_with_the_quay_operator/index
[2]:	https://redhatgov.io
[3]:	https://github.com/jilleJr
[4]:	https://start.learning.redhat.com/totara/1929
[5]:	https://red.ht/ARORHPDS