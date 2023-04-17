let legs_json = {
    "nodes": [
        {
            "id": "1-1-1",
            "surface_number": "1-1",
            "png": "../static/img/gan_images/1-1-1.png",
            "multi_figured_composition": 1.0,
            "other_creatures": 0.0
        },
        {
            "id": "1-2-1",
            "surface_number": "1-2",
            "png": "../static/img/gan_images/1-2-1.png",
            "multi_figured_composition": 1.0,
            "other_creatures": 1.0
        },
        {
            "id": "1-3-1",
            "surface_number": "1-3",
            "png": "../static/img/gan_images/1-3-1.png",
            "multi_figured_composition": 1.0,
            "other_creatures": 1.0
        },
        {
            "id": "1-3-2",
            "surface_number": "1-3",
            "png": "../static/img/gan_images/1-3-2.png",
            "multi_figured_composition": 1.0,
            "other_creatures": 1.0
        },
    ],
    "links": [
        {
            "source": "1-1-1",
            "target": "1-2-1",
            "weight": 5.0
        },
        {
            "source": "1-1-1",
            "target": "1-3-1",
            "weight": 4.0
        },
        {
            "source": "1-1-1",
            "target": "1-3-2",
            "weight": 3.0
        }]
}

const Graph = ForceGraph()
    (document.getElementById('graph'))
    .graphData(legs_json)
    .nodeId('id')
    // .nodeVal('val')
    .nodeLabel('id')
    .nodeAutoColorBy('surface_number')
    .linkSource('source')
    .linkTarget('target')
    .linkWidth('weight')
    .linkColor('color')
    .nodeRelSize(8)
    // .onNodeClick()
    .nodeCanvasObject((node, ctx, globalScale) => {
        const size = 12;
        const img = new Image();
        img.src = node.png;
        ctx.drawImage(img, node.x - size / 2, node.y - size / 2, size, size);
    }
    )