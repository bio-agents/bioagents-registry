# Credit for this script to Alban Gaignard
# https://github.com/albangaignard
import json


def rdfize(entry):
    """
    Transforms a bioagents json entry into RDF, and returns a JSON-LD serialization. The following fields
    are covered: contact, publication, EDAM topic, EDAM operation, EDAM inputs & outputs.
    """
    jsonld = {}

    try:
        ctx = {
            "@context": {
                "@base": "https://bioagents.tech/",
                "bioagents": "https://bioagents.tech/ontology/",
                "edam": "http://edamontology.org/",
                "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
                "sc": "http://schema.org/",
                "dct": "http://purl.org/dc/terms/",
                "bsc": "http://bioschemas.org/",
                "bsct": "http://bioschemas.org/types/",
                "description": "sc:description",
                "name": "sc:name",
                "identifier": "sc:identifier",
                "sameAs": "sc:sameAs",
                "homepage": "sc:url",
                "agentType": "sc:additionalType",
                "primaryContact": "bioagents:primaryContact",
                "author": "sc:author",
                "provider": "sc:provider",
                "contributor": "sc:contributor",
                "funder": "sc:funder",
                "hasPublication": "sc:citation",
                "hasTopic": "sc:applicationSubCategory",
                "hasOperation": "sc:featureList",
                "hasInputData": "bsc:input",
                "hasOutputData": "bsc:output",
                "license": "sc:license",
                "version": "sc:softwareVersion",
                "isAccessibleForFree": "sc:isAccessibleForFree",
                "operatingSystem": "sc:operatingSystem",
                "hasApiDoc": "sc:softwareHelp",
                "hasGenDoc": "sc:softwareHelp",
                "hasTermsOfUse": "sc:termsOfService",
                "conformsTo": "dct:conformsTo",
            }
        }
        objects = []
        graph = {"@graph": objects}
        jsonld.update(ctx)
        jsonld.update(graph)

        agent = {}
        agent["@id"] = str(entry["bioagentsID"])
        agent["@type"] = ["sc:SoftwareApplication"]
        agent["applicationCategory"] = "Computational science agent"
        agent["primaryContact"] = []
        agent["author"] = []
        agent["contributor"] = []
        agent["provider"] = []
        agent["funder"] = []
        agent[
            "conformsTo"
        ] = "https://bioschemas.org/profiles/ComputationalAgent/1.0-RELEASE"

        if entry.get("credit"):
            for credit in entry["credit"]:
                # print(credit)
                ## Retrieving FUNDERS
                if "typeEntity" in credit.keys() and credit["typeEntity"]:
                    if "Funding agency" in credit["typeEntity"]:
                        sType = "schema:Organization"
                        if "orcidid" in credit.keys() and credit["orcidid"] != None:
                            if not "funder" in agent.keys():
                                agent["funder"] = {
                                    "@id": credit["orcidid"],
                                    "@type": sType,
                                }
                            else:
                                agent["funder"].append(
                                    {"@id": credit["orcidid"], "@type": sType}
                                )
                        elif "name" in credit.keys() and credit["name"] != None:
                            if not "funder" in agent.keys():
                                agent["funder"] = [credit["name"]]
                            else:
                                agent["funder"].append(credit["name"])

                # Retrieving CONTRIBUTORS, PROVIDERS, DEVELOPERS
                if credit.get("typeRole"):
                    if "Developer" in credit["typeRole"]:
                        # print("**** DEVELOPER ****")
                        # print(credit['name'])
                        if "typeEntity" in credit.keys() and credit["typeEntity"]:
                            if "Person" in credit["typeEntity"]:
                                sType = "schema:Person"
                            else:
                                sType = "schema:Organization"
                            if "orcidid" in credit.keys() and credit["orcidid"] != None:
                                if not "author" in agent.keys():
                                    agent["author"] = {
                                        "@id": credit["orcidid"],
                                        "@type": sType,
                                    }
                                else:
                                    agent["author"].append(
                                        {"@id": credit["orcidid"], "@type": sType}
                                    )
                            elif "name" in credit.keys() and credit["name"] != None:
                                if not "author" in agent.keys():
                                    agent["author"] = [credit["name"]]
                                else:
                                    agent["author"].append(credit["name"])
                        else:
                            if "name" in credit.keys() and credit["name"] != None:
                                if not "author" in agent.keys():
                                    agent["author"] = [credit["name"]]
                                else:
                                    agent["author"].append(credit["name"])

                    if "Provider" in credit["typeRole"]:
                        # print("**** PROVIDER ****")
                        # print(credit['name'])
                        if "typeEntity" in credit.keys() and credit["typeEntity"]:
                            if "Person" in credit["typeEntity"]:
                                sType = "schema:Person"
                            else:
                                sType = "schema:Organization"

                            if "orcidid" in credit.keys() and credit["orcidid"] != None:
                                if not "provider" in agent.keys():
                                    agent["provider"] = {
                                        "@id": credit["orcidid"],
                                        "@type": sType,
                                    }
                                else:
                                    agent["provider"].append(
                                        {"@id": credit["orcidid"], "@type": sType}
                                    )
                            elif "name" in credit.keys() and credit["name"] != None:
                                if not "provider" in agent.keys():
                                    agent["provider"] = [credit["name"]]
                                else:
                                    agent["provider"].append(credit["name"])
                        else:
                            if "name" in credit.keys() and credit["name"] != None:
                                if not "provider" in agent.keys():
                                    agent["provider"] = [credit["name"]]
                                else:
                                    agent["provider"].append(credit["name"])

                    if "Contributor" in credit["typeRole"]:

                        if "typeEntity" in credit.keys() and credit["typeEntity"]:
                            if "Person" in credit["typeEntity"]:
                                sType = "schema:Person"
                            else:
                                sType = "schema:Organization"

                            if "orcidid" in credit.keys() and credit["orcidid"] != None:
                                if not "contributor" in agent.keys():
                                    agent["contributor"] = {
                                        "@id": credit["orcidid"],
                                        "@type": sType,
                                    }
                                else:
                                    agent["contributor"].append(
                                        {"@id": credit["orcidid"], "@type": sType}
                                    )
                            elif "name" in credit.keys() and credit["name"] != None:
                                if not "contributor" in agent.keys():
                                    agent["contributor"] = [credit["name"]]
                                else:
                                    agent["contributor"].append(credit["name"])
                        else:
                            if "name" in credit.keys() and credit["name"] != None:
                                if not "contributor" in agent.keys():
                                    agent["contributor"] = [credit["name"]]
                                else:
                                    agent["contributor"].append(credit["name"])

                    if "Primary contact" in credit["typeRole"]:
                        if "typeEntity" in credit.keys() and credit["typeEntity"]:
                            if "Person" in credit["typeEntity"]:
                                sType = "schema:Person"
                            else:
                                sType = "schema:Organization"

                            if "orcidid" in credit.keys() and credit["orcidid"] != None:
                                if not "primaryContact" in agent.keys():
                                    agent["primaryContact"] = {
                                        "@id": credit["orcidid"],
                                        "@type": sType,
                                    }
                                else:
                                    agent["primaryContact"].append(
                                        {"@id": credit["orcidid"], "@type": sType}
                                    )
                            elif "name" in credit.keys() and credit["name"] != None:
                                if not "primaryContact" in agent.keys():
                                    agent["primaryContact"] = [credit["name"]]
                                else:
                                    agent["primaryContact"].append(credit["name"])
                        else:
                            if "name" in credit.keys() and credit["name"] != None:
                                if not "primaryContact" in agent.keys():
                                    agent["primaryContact"] = [credit["name"]]
                                else:
                                    agent["primaryContact"].append(credit["name"])

        if entry.get("publication"):
            for publication in entry["publication"]:
                if publication.get("pmid"):
                    if not "hasPublication" in agent.keys():
                        agent["hasPublication"] = ["pubmed:" + publication["pmid"]]
                    else:
                        agent["hasPublication"].append("pubmed:" + publication["pmid"])
                if publication.get("pmcid"):
                    if not "hasPublication" in agent.keys():
                        agent["hasPublication"] = ["pmcid:" + publication["pmcid"]]
                    else:
                        agent["hasPublication"].append("pmcid:" + publication["pmcid"])
                if publication.get("doi"):
                    if not ("<" in publication["doi"] or ">" in publication["doi"]):
                        if not "hasPublication" in agent.keys():
                            agent["hasPublication"] = [
                                {
                                    "@id": "https://doi.org/" + publication["doi"],
                                    "@type": "sc:CreativeWork",
                                }
                            ]
                        else:
                            agent["hasPublication"].append(
                                {
                                    "@id": "https://doi.org/" + publication["doi"],
                                    "@type": "sc:CreativeWork",
                                }
                            )

        if entry.get("function"):
            counter_op = 0
            for item in entry["function"]:
                counter_op += 1
                if item.get("operation"):
                    for op in item["operation"]:
                        if not "hasOperation" in agent.keys():
                            agent["hasOperation"] = [{"@id": op["uri"]}]
                        else:
                            agent["hasOperation"].append({"@id": op["uri"]})

                if item.get("input"):
                    counter_in = 0
                    for input in item["input"]:
                        counter_in += 1
                        input_object = {
                            "@id": agent["@id"]
                            + "/op_"
                            + str(counter_op)
                            + "/in_"
                            + str(counter_in),
                            "@type": "bsct:FormalParameter",
                            "name": input["data"]["term"],
                            "identifier": input["data"]["uri"],
                            "sameAs": input["data"]["uri"],
                        }
                        if not "hasInputData" in agent.keys():
                            agent["hasInputData"] = [input_object]
                        else:
                            agent["hasInputData"].append(input_object)

                if item.get("output"):
                    counter_out = 0
                    for output in item["output"]:
                        counter_out += 1
                        output_object = {
                            "@id": agent["@id"]
                            + "/op_"
                            + str(counter_op)
                            + "/in_"
                            + str(counter_out),
                            "@type": "bsct:FormalParameter",
                            "name": output["data"]["term"],
                            "identifier": output["data"]["uri"],
                            "sameAs": output["data"]["uri"],
                        }
                        if not "hasOutputData" in agent.keys():
                            agent["hasOutputData"] = [output_object]
                        else:
                            agent["hasOutputData"].append(output_object)

        if entry.get("topic"):
            for item in entry["topic"]:
                if not "hasTopic" in agent.keys():
                    agent["hasTopic"] = [{"@id": item["uri"]}]
                else:
                    agent["hasTopic"].append({"@id": item["uri"]})

        if entry.get("cost"):
            for item in entry["cost"]:
                if not "isAccessibleForFree" in agent.keys():
                    if "Free" in entry["cost"]:
                        agent["isAccessibleForFree"] = True
                    else:
                        agent["isAccessibleForFree"] = False

        if entry.get("documentation"):
            for item in entry["documentation"]:
                if "type" in item.keys() and item["type"]:
                    item["url"] = item["url"].replace("|", "%7C")
                    if "API" in item["type"]:
                        if not "hasApiDoc" in agent.keys():
                            agent["hasApiDoc"] = [{"@id": item["url"]}]
                        else:
                            agent["hasApiDoc"].append({"@id": item["url"]})
                    elif "Terms" in item["type"]:
                        if not "hasTermsOfUse" in agent.keys():
                            agent["hasTermsOfUse"] = [{"@id": item["url"]}]
                        else:
                            agent["hasTermsOfUse"].append({"@id": item["url"]})
                    else:
                        if not "hasGenDoc" in agent.keys():
                            agent["hasGenDoc"] = [{"@id": item["url"]}]
                        else:
                            agent["hasGenDoc"].append({"@id": item["url"]})

    except KeyError as e:
        print(e)
        pass

    graph["@graph"] = agent
    jsonld.update(graph)
    # print(json.dumps(jsonld, indent=4, sort_keys=True))
    # raw_jld = json.dumps(entry, indent=4, sort_keys=True)
    return jsonld
