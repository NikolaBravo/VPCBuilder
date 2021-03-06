import unittest
import json
import yaml
import cfnlint.core
import os
import src.macro
from mock import MagicMock


class TestVPCBuilderFragmentLinterSetup(unittest.TestCase):
    identifier = "TEST"

    def setUp(self):
        self.maxDiff = None


class TestVPCBuilderFragmentLinter(TestVPCBuilderFragmentLinterSetup):

    def test_macro_all_objects(self):

        template_path = "tests"
        template_filename = "template.json"

        transform_call = {
            "transformId": "801604450668::VPC",
            "templateParameterValues": {
                "VGW": "vgw-06bbcf429c1cb0eed"
            },
            "fragment": {
                "AWSTemplateFormatVersion": "2010-09-09",
                "Resources": {
                    "KABLAMOBUILDVPC": {
                        "Type": "Elendel::Network::VPC",
                        "Properties": {
                            "Subnets": {
                                "ReservedMgmt1": {
                                    "CIDR": "172.16.0.0/26",
                                    "AZ": 0,
                                    "NetACL": "InternalSubnetAcl",
                                    "RouteTable": "InternalRT1"
                                },
                                "ReservedMgmt2": {
                                    "CIDR": "172.16.1.0/26",
                                    "AZ": 1,
                                    "NetACL": "InternalSubnetAcl",
                                    "RouteTable": "InternalRT2"
                                },
                                "ReservedMgmt3": {
                                    "CIDR": "172.16.2.0/26",
                                    "AZ": 2,
                                    "NetACL": "InternalSubnetAcl",
                                    "RouteTable": "InternalRT3"
                                },
                                "Internal1": {
                                    "CIDR": "172.16.3.0/24",
                                    "AZ": 0,
                                    "NetACL": "InternalSubnetAcl",
                                    "RouteTable": "InternalRT1"
                                },
                                "Internal2": {
                                    "CIDR": "172.16.4.0/24",
                                    "AZ": 1,
                                    "NetACL": "InternalSubnetAcl",
                                    "RouteTable": "InternalRT2"
                                },
                                "Internal3": {
                                    "CIDR": "172.16.5.0/24",
                                    "AZ": 2,
                                    "NetACL": "InternalSubnetAcl",
                                    "RouteTable": "InternalRT3"
                                },
                                "ReservedNet3": {
                                    "CIDR": "172.16.2.192/26",
                                    "AZ": 2,
                                    "NetACL": "RestrictedSubnetAcl",
                                    "RouteTable": "PublicRT"
                                },
                                "ReservedNet2": {
                                    "CIDR": "172.16.1.192/26",
                                    "AZ": 1,
                                    "NetACL": "RestrictedSubnetAcl",
                                    "RouteTable": "PublicRT"
                                },
                                "ReservedNet1": {
                                    "CIDR": "172.16.0.192/26",
                                    "AZ": 0,
                                    "NetACL": "RestrictedSubnetAcl",
                                    "RouteTable": "PublicRT"
                                },
                                "PerimeterInternal1": {
                                    "CIDR": "172.16.6.0/24",
                                    "AZ": 0,
                                    "NetACL": "InternalSubnetAcl",
                                    "RouteTable": "InternalRT1"
                                },
                                "PerimeterInternal2": {
                                    "CIDR": "172.16.7.0/24",
                                    "AZ": 1,
                                    "NetACL": "InternalSubnetAcl",
                                    "RouteTable": "InternalRT2"
                                },
                                "PerimeterInternal3": {
                                    "CIDR": "172.16.8.0/24",
                                    "AZ": 2,
                                    "NetACL": "InternalSubnetAcl",
                                    "RouteTable": "InternalRT3"
                                }
                            },
                            "TransitGateways": {
                                "Test1": {
                                    "Subnets": [
                                        "Internal1",
                                        "Internal2",
                                        "Internal3"
                                    ],
                                    "TransitGatewayId": "tgw-01234567890123456",
                                    "Tags": {
                                        "Name": "PRIVATE-EGRESS-VPC-TGW1",
                                        "Purpose": "Gateway Attach 1"
                                    }
                                },
                                "Test2": {
                                    "Subnets": [
                                        "Internal1",
                                        "Internal2",
                                        "Internal3"
                                    ],
                                    "TransitGatewayId": "tgw-98765432109876543",
                                    "Tags": {
                                        "Name": "PRIVATE-EGRESS-VPC-TGW2",
                                        "Purpose": "Gateway Attach 2"
                                    }
                                }
                            },
                            "Tags": {
                                "Name": "PRIVATE-EGRESS-VPC",
                                "Template": "VPC for private endpoints egress only"
                            },
                            "NATGateways": {
                                "NATGW3": {
                                    "Subnet": "ReservedNet3",
                                    "Routetable": "InternalRT3"
                                },
                                "NATGW2": {
                                    "Subnet": "ReservedNet2",
                                    "Routetable": "InternalRT2"
                                },
                                "NATGW1": {
                                    "Subnet": "ReservedNet1",
                                    "Routetable": "InternalRT1"
                                }
                            },
                            "NetworkACLs": {
                                "InternalSubnetAcl": {
                                    "InternalSubnetAclEntryOutTCPUnreserved": "106,6,allow,true,172.16.0.0/16,1024,65535",
                                    "InternalSubnetAclEntryOutUDPDNSIPv6": "113,17,allow,true,::/0,53,53",
                                    "InternalSubnetAclEntryOutUDPUnreserved": "107,6,allow,true,172.16.0.0/16,1024,65535",
                                    "InternalSubnetAclEntryOut": "100,-1,allow,true,172.16.0.0/16,1,65535",
                                    "InternalSubnetAclEntryOutSSH": "150,6,allow,true,0.0.0.0/0,22,22",
                                    "InternalSubnetAclEntryInUDPUnreservedIPv6": "105,17,allow,false,::/0,1024,65535",
                                    "InternalSubnetAclEntryOutTCPDNSIPv6": "112,6,allow,true,::/0,53,53",
                                    "InternalSubnetAclEntryOutTCPDNS": "110,6,allow,true,0.0.0.0/0,53,53",
                                    "InternalSubnetAclEntryOutHTTPS": "103,6,allow,true,0.0.0.0/0,443,443",
                                    "InternalSubnetAclEntryOutHTTP": "102,6,allow,true,0.0.0.0/0,80,80",
                                    "InternalSubnetAclEntryOutHTTPIPv6": "104,6,allow,true,::/0,80,80",
                                    "InternalSubnetAclEntryOutHTTPSIPv6": "105,6,allow,true,::/0,443,443",
                                    "InternalSubnetAclEntryInTCPUnreservedIPv6": "104,6,allow,false,::/0,1024,65535",
                                    "InternalSubnetAclEntryOutUDPDNS": "111,17,allow,true,0.0.0.0/0,53,53",
                                    "InternalSubnetAclEntryIn": "100,-1,allow,false,172.16.0.0/16,1,65535",
                                    "InternalSubnetAclEntryInTCPUnreserved": "102,6,allow,false,0.0.0.0/0,1024,65535",
                                    "InternalSubnetAclEntryInUDPUnreserved": "103,17,allow,false,0.0.0.0/0,1024,65535"
                                },
                                "RestrictedSubnetAcl": {
                                    "RestrictedSubnetAclEntryInUDPUnReserved": "91,17,allow,false,0.0.0.0/0,1024,65535",
                                    "RestrictedSubnetAclEntryOutSSH": "103,6,allow,true,0.0.0.0/0,22,22",
                                    "RestrictedSubnetAclEntryOutDNSTCPIPv6": "151,6,allow,true,::/0,53,53",
                                    "RestrictedSubnetAclEntryOutHTTPSIPv6": "105,6,allow,true,::/0,443,443",
                                    "RestrictedSubnetAclEntryInTCPUnReservedIPv6": "92,6,allow,false,::/0,1024,65535",
                                    "RestrictedSubnetAclEntryNTP": "120,6,allow,true,0.0.0.0/0,123,123",
                                    "RestrictedSubnetAclEntryOutPuppet": "94,6,allow,true,172.16.0.0/16,8140,8140",
                                    "RestrictedSubnetAclEntryIn": "110,-1,allow,false,172.16.0.0/16,1,65535",
                                    "RestrictedSubnetAclEntryOutHTTP": "101,6,allow,true,0.0.0.0/0,80,80",
                                    "RestrictedSubnetAclEntryInHTTPSIPv6": "104,6,allow,false,::/0,443,443",
                                    "RestrictedSubnetAclEntryInNetBios": "170,6,allow,false,172.16.0.0/16,389,389",
                                    "RestrictedSubnetAclEntryOutDNSTCP": "150,6,allow,true,0.0.0.0/0,53,53",
                                    "RestrictedSubnetAclEntryInUDPUnReservedIPv6": "93,17,allow,false,::/0,1024,65535",
                                    "RestrictedSubnetAclEntryInHTTP": "101,6,allow,false,0.0.0.0/0,80,80",
                                    "RestrictedSubnetAclEntryInHTTPIPv6": "103,6,allow,false,::/0,80,80",
                                    "RestrictedSubnetAclEntryOutDNSUDP": "160,17,allow,true,0.0.0.0/0,53,53",
                                    "RestrictedSubnetAclEntryInTCPUnReserved": "90,6,allow,false,0.0.0.0/0,1024,65535",
                                    "RestrictedSubnetAclEntryOutTCPUnReserved": "90,6,allow,true,0.0.0.0/0,1024,65535",
                                    "RestrictedSubnetAclEntryInDNSTCP": "150,6,allow,false,172.16.0.0/16,53,53",
                                    "RestrictedSubnetAclEntryOutUDPUnReservedIPv6": "93,17,allow,true,::/0,1024,65535",
                                    "RestrictedSubnetAclEntryOutNetBios1": "180,6,allow,true,172.16.0.0/16,137,139",
                                    "RestrictedSubnetAclEntryOut": "110,-1,allow,true,172.16.0.0/16,1,65535",
                                    "RestrictedSubnetAclEntryOutHTTPIPv6": "104,6,allow,true,::/0,80,80",
                                    "RestrictedSubnetAclEntryOutHTTPS": "102,6,allow,true,0.0.0.0/0,443,443",
                                    "RestrictedSubnetAclEntryOutNetBios": "170,6,allow,true,172.16.0.0/16,389,389",
                                    "RestrictedSubnetAclEntryOutTCPUnReservedIPv6": "92,6,allow,true,::/0,1024,65535",
                                    "RestrictedSubnetAclEntryOutUDPUnReserved": "91,17,allow,true,0.0.0.0/0,1024,65535",
                                    "RestrictedSubnetAclEntryInNetBios1": "80,6,allow,false,172.16.0.0/16,137,139",
                                    "RestrictedSubnetAclEntryOutSSHIPv6": "106,6,allow,true,::/0,22,22",
                                    "RestrictedSubnetAclEntryInHTTPS": "102,6,allow,false,0.0.0.0/0,443,443",
                                    "RestrictedSubnetAclEntryInDNSUDP": "160,17,allow,false,172.16.0.0/16,53,53",
                                    "RestrictedSubnetAclEntryOutDNSUDPIPv6": "161,17,allow,true,::/0,53,53",
                                    "RestrictedSubnetAclEntryInSquid2": "140,6,allow,false,172.16.0.0/16,3128,3128"
                                }
                            },
                            "SecurityGroups": {
                                "VPCEndpoint": {
                                    "SecurityGroupIngress": [
                                        [
                                            "icmp",
                                            -1,
                                            -1,
                                            "172.16.0.0/20",
                                            "All ICMP Traffic"
                                        ],
                                        [
                                            "tcp",
                                            0,
                                            65535,
                                            "172.16.0.0/20",
                                            "All TCP Traffic"
                                        ],
                                        [
                                            "udp",
                                            0,
                                            65535,
                                            "172.16.0.0/20",
                                            "All UDP Traffic"
                                        ]
                                    ],
                                    "Tags": {
                                        "Name": "VPCEndpoint"
                                    },
                                    "GroupDescription": "VPC Endpoint Interface Firewall Rules",
                                    "SecurityGroupEgress": [
                                        [
                                            "icmp",
                                            -1,
                                            -1,
                                            "172.16.0.0/20",
                                            "All ICMP Traffic"
                                        ],
                                        [
                                            "tcp",
                                            0,
                                            65535,
                                            "172.16.0.0/20",
                                            "All TCP Traffic"
                                        ],
                                        [
                                            "udp",
                                            0,
                                            65535,
                                            "172.16.0.0/20",
                                            "All UDP Traffic"
                                        ]
                                    ]
                                }
                            },
                            "Details": {
                                "VPCDesc": "Private Egress VPC",
                                "Region": "ap-southeast-2",
                                "VPCName": "PRIVATEEGRESSVPC",
                                "IPv6": "true"
                            },
                            "DHCP": {
                                "NTPServers": "169.254.169.123",
                                "NTBType": 2,
                                "Name": "DhcpOptions",
                                "DNSServers": "172.16.0.2"
                            },
                            "CIDR": "172.16.0.0/20",
                            "Endpoints": {
                                "kinesis-streams": {
                                    "SubnetIds": [
                                        "ReservedMgmt1",
                                        "ReservedMgmt2",
                                        "ReservedMgmt3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "cloudtrail": {
                                    "SubnetIds": [
                                        "ReservedMgmt1",
                                        "ReservedMgmt2",
                                        "ReservedMgmt3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "cloudformation": {
                                    "SubnetIds": [
                                        "ReservedMgmt1",
                                        "ReservedMgmt2",
                                        "ReservedMgmt3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "elasticloadbalancing": {
                                    "SubnetIds": [
                                        "ReservedMgmt1",
                                        "ReservedMgmt2",
                                        "ReservedMgmt3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "ec2": {
                                    "SubnetIds": [
                                        "ReservedMgmt1",
                                        "ReservedMgmt2",
                                        "ReservedMgmt3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "logs": {
                                    "SubnetIds": [
                                        "ReservedMgmt1",
                                        "ReservedMgmt2",
                                        "ReservedMgmt3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "monitoring": {
                                    "SubnetIds": [
                                        "ReservedMgmt1",
                                        "ReservedMgmt2",
                                        "ReservedMgmt3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "s3": {
                                    "RouteTableIds": [
                                        "PublicRT",
                                        "InternalRT1",
                                        "InternalRT2",
                                        "InternalRT3"
                                    ],
                                    "PolicyDocument": "{\n    \"Version\":\"2012-10-17\",\n    \"Statement\":[\n        {\n            \"Effect\":\"Allow\",\n            \"Principal\": \"*\",\n            \"Action\":[\"s3:*\"],\n            \"Resource\":[\"*\"]\n        }\n    ]\n}\n",
                                    "Type": "Gateway"
                                },
                                "dynamodb": {
                                    "RouteTableIds": [
                                        "PublicRT",
                                        "InternalRT1",
                                        "InternalRT2",
                                        "InternalRT3"
                                    ],
                                    "PolicyDocument": "{\n    \"Version\":\"2012-10-17\",\n    \"Statement\":[\n        {\n            \"Effect\":\"Allow\",\n            \"Principal\": \"*\",\n            \"Action\":[\"s3:*\"],\n            \"Resource\":[\"*\"]\n        }\n    ]\n}\n",
                                    "Type": "Gateway"
                                },
                                "ec2messages": {
                                    "SubnetIds": [
                                        "ReservedMgmt1",
                                        "ReservedMgmt2",
                                        "ReservedMgmt3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "kms": {
                                    "SubnetIds": [
                                        "ReservedMgmt1",
                                        "ReservedMgmt2",
                                        "ReservedMgmt3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "config": {
                                    "SubnetIds": [
                                        "ReservedMgmt1",
                                        "ReservedMgmt2",
                                        "ReservedMgmt3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "events": {
                                    "SubnetIds": [
                                        "ReservedMgmt1",
                                        "ReservedMgmt2",
                                        "ReservedMgmt3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "sagemaker.api": {
                                    "SubnetIds": [
                                        "ReservedMgmt1",
                                        "ReservedMgmt2",
                                        "ReservedMgmt3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "ssm": {
                                    "SubnetIds": [
                                        "ReservedMgmt1",
                                        "ReservedMgmt2",
                                        "ReservedMgmt3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "sns": {
                                    "SubnetIds": [
                                        "ReservedMgmt1",
                                        "ReservedMgmt2",
                                        "ReservedMgmt3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "sagemaker.runtime": {
                                    "SubnetIds": [
                                        "ReservedMgmt1",
                                        "ReservedMgmt2",
                                        "ReservedMgmt3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "codebuild": {
                                    "SubnetIds": [
                                        "ReservedMgmt1",
                                        "ReservedMgmt2",
                                        "ReservedMgmt3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "servicecatalog": {
                                    "SubnetIds": [
                                        "ReservedMgmt1",
                                        "ReservedMgmt2",
                                        "ReservedMgmt3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "execute-api": {
                                    "SubnetIds": [
                                        "ReservedMgmt1",
                                        "ReservedMgmt2",
                                        "ReservedMgmt3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "secretsmanager": {
                                    "SubnetIds": [
                                        "ReservedMgmt1",
                                        "ReservedMgmt2",
                                        "ReservedMgmt3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "ssmmessages": {
                                    "SubnetIds": [
                                        "ReservedMgmt1",
                                        "ReservedMgmt2",
                                        "ReservedMgmt3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                }
                            },
                            "RouteTables": {
                                "InternalRT3": "",
                                "PublicRT": [
                                    {
                                        "RouteName": "PublicRoute",
                                        "RouteCIDR": "0.0.0.0/0",
                                        "RouteGW": "InternetGateway"
                                    },
                                    {
                                        "RouteName": "PublicRouteIPv6",
                                        "RouteCIDR": "::/0",
                                        "RouteGW": "InternetGateway"
                                    }
                                ],
                                "InternalRT2": "",
                                "InternalRT1": ""
                            }
                        }
                    }
                },
                "Description": "Private VPC Template",
                "Parameters": {
                    "VGW": {
                        "Default": "vgw-012345678",
                        "Type": "String",
                        "Description": "VPC Gateway"
                    }
                },
                "Mappings": {}
            },
            "region": "us-east-1",
            "params": {},
            "requestId": "508122ef-6442-46eb-b2fc-5fab1f4f7064",
            "accountId": "012345678901"
        }

        actual = src.macro.handler(transform_call, "")

        with open(os.path.join(template_path, template_filename), "wb") as fh:
            fh.write(json.dumps(actual['fragment'], sort_keys=True, indent=4, separators=(',', ': ')))

        template = cfnlint.decode.cfn_json.load(template_path + "/" + template_filename)

        rules = cfnlint.core.get_rules([], [], [])

        results = []
        results.extend(
            cfnlint.core.run_checks(
                template_filename, template, rules, ['us-east-1']))

        self.assertEqual(results, [])
