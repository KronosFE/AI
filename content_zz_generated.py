# -*- coding: utf-8 -*-
"""Loader for agent-generated pages. Multi-agent build writes JSON page arrays to
ai/_gen/*.json; this module registers them all into the generator. Each object:
{slug,title,cat,lede,body,related,[gate],[facts],[seo_type]} where body is a list
of [type,value] pairs (h2,h3,p,ul,code,matrix,truth,circuit,clip,html)."""
import os, json, glob
HERE = os.path.dirname(os.path.abspath(__file__))

def register(add, F):
    for fp in sorted(glob.glob(os.path.join(HERE, "_gen", "*.json"))):
        try:
            data = json.load(open(fp, encoding="utf-8"))
        except Exception as e:
            print("  [gen] skip", os.path.basename(fp), e); continue
        for p in data:
            # normalize body pairs (JSON gives lists; renderer expects tuples)
            p["body"] = [tuple(b) for b in p.get("body", [])]
            if p.get("related"): p["related"] = [tuple(r) for r in p["related"]]
            if p.get("facts"): p["facts"] = [tuple(f) for f in p["facts"]]
            p.setdefault("seo_type", "TechArticle")
            add(p)
