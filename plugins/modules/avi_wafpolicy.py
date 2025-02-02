#!/usr/bin/python
# module_check: supported

# Copyright 2021 VMware, Inc.  All rights reserved. VMware Confidential
# SPDX-License-Identifier: Apache License 2.0

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: avi_wafpolicy
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of WafPolicy Avi RESTful Object
description:
    - This module is used to configure WafPolicy object
    - more examples at U(https://github.com/avinetworks/devops)
options:
    state:
        description:
            - The state that should be applied on the entity.
        default: present
        choices: ["absent", "present"]
        type: str
    avi_api_update_method:
        description:
            - Default method for object update is HTTP PUT.
            - Setting to patch will override that behavior to use HTTP PATCH.
        default: put
        choices: ["put", "patch"]
        type: str
    avi_api_patch_op:
        description:
            - Patch operation to use when using avi_api_update_method as patch.
        choices: ["add", "replace", "delete", "remove"]
        type: str
    avi_patch_path:
        description:
            - Patch path to use when using avi_api_update_method as patch.
        type: str
    avi_patch_value:
        description:
            - Patch value to use when using avi_api_update_method as patch.
        type: str
    allow_mode_delegation:
        description:
            - Allow rules to overwrite the policy mode.
            - This must be set if the policy mode is set to enforcement.
            - Field introduced in 18.1.5, 18.2.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    allowlist:
        description:
            - A set of rules which describe conditions under which the request will bypass the waf.
            - This will be processed in the request header phase before any other waf related code.
            - Field introduced in 20.1.3.
        type: dict
    application_signatures:
        description:
            - Application specific signatures.
            - Field introduced in 20.1.1.
        type: dict
    confidence_override:
        description:
            - Configure thresholds for confidence labels.
            - Field introduced in 20.1.1.
        type: dict
    configpb_attributes:
        description:
            - Protobuf versioning for config pbs.
            - Field introduced in 21.1.1.
        type: dict
    created_by:
        description:
            - Creator name.
            - Field introduced in 17.2.4.
        type: str
    crs_groups:
        description:
            - This entry is deprecated.
            - If you want to change the property of a crs group or rule (enabled, mode, exclusions), please use the crs_overrides field instead.
            - Field deprecated in 20.1.6.
            - Field introduced in 17.2.1.
        type: list
    crs_overrides:
        description:
            - Override attributes for crs rules.
            - Field introduced in 20.1.6.
        type: list
    description:
        description:
            - Field introduced in 17.2.1.
        type: str
    enable_app_learning:
        description:
            - Enable application learning for this waf policy.
            - Field introduced in 18.2.3.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    enable_auto_rule_updates:
        description:
            - Enable application learning based rule updates on the waf profile.
            - Rules will be programmed in dedicated waf learning group.
            - Field introduced in 20.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    enable_regex_learning:
        description:
            - Enable dynamic regex generation for positive security model rules.
            - This is an experimental feature and shouldn't be used in production.
            - Field introduced in 20.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    failure_mode:
        description:
            - Waf policy failure mode.
            - This can be 'open' or 'closed'.
            - Enum options - WAF_FAILURE_MODE_OPEN, WAF_FAILURE_MODE_CLOSED.
            - Field introduced in 18.1.2.
            - Default value when not specified in API or module is interpreted by Avi Controller as WAF_FAILURE_MODE_OPEN.
        type: str
    geo_db_ref:
        description:
            - Geo location mapping database used by this wafpolicy.
            - It is a reference to an object of type geodb.
            - Field introduced in 21.1.1.
        type: str
    labels:
        description:
            - Key value pairs for granular object access control.
            - Also allows for classification and tagging of similar objects.
            - Field deprecated in 20.1.5.
            - Field introduced in 20.1.2.
            - Maximum of 4 items allowed.
        type: list
    learning:
        description:
            - Configure parameters for waf learning.
            - Field deprecated in 18.2.3.
            - Field introduced in 18.1.2.
        type: dict
    learning_params:
        description:
            - Parameters for tuning application learning.
            - Field introduced in 20.1.1.
        type: dict
    markers:
        description:
            - List of labels to be used for granular rbac.
            - Field introduced in 20.1.5.
            - Allowed in basic edition, essentials edition, enterprise edition.
        type: list
    min_confidence:
        description:
            - Minimum confidence label required for auto rule updates.
            - Enum options - CONFIDENCE_VERY_HIGH, CONFIDENCE_HIGH, CONFIDENCE_PROBABLE, CONFIDENCE_LOW, CONFIDENCE_NONE.
            - Field introduced in 20.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as CONFIDENCE_VERY_HIGH.
        type: str
    mode:
        description:
            - Waf policy mode.
            - This can be detection or enforcement.
            - It can be overwritten by rules if allow_mode_delegation is set.
            - Enum options - WAF_MODE_DETECTION_ONLY, WAF_MODE_ENFORCEMENT.
            - Field introduced in 17.2.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as WAF_MODE_DETECTION_ONLY.
        type: str
    name:
        description:
            - Field introduced in 17.2.1.
        required: true
        type: str
    paranoia_level:
        description:
            - Waf ruleset paranoia  mode.
            - This is used to select rules based on the paranoia-level tag.
            - Enum options - WAF_PARANOIA_LEVEL_LOW, WAF_PARANOIA_LEVEL_MEDIUM, WAF_PARANOIA_LEVEL_HIGH, WAF_PARANOIA_LEVEL_EXTREME.
            - Field introduced in 17.2.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as WAF_PARANOIA_LEVEL_LOW.
        type: str
    positive_security_model:
        description:
            - The positive security model.
            - This is used to describe how the request or parts of the request should look like.
            - It is executed in the request body phase of avi waf.
            - Field introduced in 18.2.3.
        type: dict
    post_crs_groups:
        description:
            - Waf rules are categorized in to groups based on their characterization.
            - These groups are created by the user and will be enforced after the crs groups.
            - Field introduced in 17.2.1.
        type: list
    pre_crs_groups:
        description:
            - Waf rules are categorized in to groups based on their characterization.
            - These groups are created by the user and will be  enforced before the crs groups.
            - Field introduced in 17.2.1.
        type: list
    resolved_crs_groups:
        description:
            - A resolved version of waf_crs_ref with waf_crs_overrides applied.
            - Field introduced in 20.1.6.
        type: list
    tenant_ref:
        description:
            - It is a reference to an object of type tenant.
            - Field introduced in 17.2.1.
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Field introduced in 17.2.1.
        type: str
    waf_crs_ref:
        description:
            - Waf core ruleset used for the crs part of this policy.
            - It is a reference to an object of type wafcrs.
            - Field introduced in 18.1.1.
        type: str
    waf_profile_ref:
        description:
            - Waf profile for waf policy.
            - It is a reference to an object of type wafprofile.
            - Field introduced in 17.2.1.
        required: true
        type: str
    whitelist:
        description:
            - A set of rules which describe conditions under which the request will bypass the waf.
            - This will be executed in the request header phase before any other waf related code.
            - Field deprecated in 20.1.3.
            - Field introduced in 18.2.3.
        type: dict
extends_documentation_fragment:
    - vmware.alb.avi
'''

EXAMPLES = """
- hosts: all
  vars:
    avi_credentials:
      username: "admin"
      password: "something"
      controller: "192.168.15.18"
      api_version: "21.1.1"

- name: Example to create WafPolicy object
  vmware.alb.avi_wafpolicy:
    avi_credentials: "{{ avi_credentials }}"
    state: present
    name: sample_wafpolicy
"""

RETURN = '''
obj:
    description: WafPolicy (api/wafpolicy) object
    returned: success, changed
    type: dict
'''

from ansible.module_utils.basic import AnsibleModule
try:
    from ansible_collections.vmware.alb.plugins.module_utils.utils.ansible_utils import (
        avi_common_argument_spec, avi_ansible_api)
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False


def main():
    argument_specs = dict(
        state=dict(default='present',
                   choices=['absent', 'present']),
        avi_api_update_method=dict(default='put',
                                   choices=['put', 'patch']),
        avi_api_patch_op=dict(choices=['add', 'replace', 'delete', 'remove']),
        avi_patch_path=dict(type='str',),
        avi_patch_value=dict(type='str',),
        allow_mode_delegation=dict(type='bool',),
        allowlist=dict(type='dict',),
        application_signatures=dict(type='dict',),
        confidence_override=dict(type='dict',),
        configpb_attributes=dict(type='dict',),
        created_by=dict(type='str',),
        crs_groups=dict(type='list',),
        crs_overrides=dict(type='list',),
        description=dict(type='str',),
        enable_app_learning=dict(type='bool',),
        enable_auto_rule_updates=dict(type='bool',),
        enable_regex_learning=dict(type='bool',),
        failure_mode=dict(type='str',),
        geo_db_ref=dict(type='str',),
        labels=dict(type='list',),
        learning=dict(type='dict',),
        learning_params=dict(type='dict',),
        markers=dict(type='list',),
        min_confidence=dict(type='str',),
        mode=dict(type='str',),
        name=dict(type='str', required=True),
        paranoia_level=dict(type='str',),
        positive_security_model=dict(type='dict',),
        post_crs_groups=dict(type='list',),
        pre_crs_groups=dict(type='list',),
        resolved_crs_groups=dict(type='list',),
        tenant_ref=dict(type='str',),
        url=dict(type='str',),
        uuid=dict(type='str',),
        waf_crs_ref=dict(type='str',),
        waf_profile_ref=dict(type='str', required=True),
        whitelist=dict(type='dict',),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_REQUESTS:
        return module.fail_json(msg=(
            'Python requests package is not installed. '
            'For installation instructions, visit https://pypi.org/project/requests.'))
    return avi_ansible_api(module, 'wafpolicy',
                           set())


if __name__ == '__main__':
    main()
