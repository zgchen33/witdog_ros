Blockly.common.defineBlocksWithJsonArray([
  {
    "type": "go_straight",
    "message0": "向 %1 行走 %2 米",
    "args0": [
      {
        "type": "field_dropdown",
        "name": "direction",
        "options": [
          [
            "前",
            "0"
          ],
          [
            "后",
            "1"
          ],
          [
            "左",
            "2"
          ],
          [
            "右",
            "3"
          ]
        ]
      },
      {
        "type": "field_number",
        "name": "distance",
        "value": 0,
        "min": 0,
        "max": 5
      }
    ],
    "previousStatement": null,
    "nextStatement": null,
    "colour": 225,
    "tooltip": "",
    "helpUrl": ""
  }
]);

Blockly.common.defineBlocksWithJsonArray([
  {
    "type": "look",
    "message0": "朝 %1 看，头部旋转 %2 度",
    "args0": [
      {
        "type": "field_dropdown",
        "name": "direction",
        "options": [
          [
            "上",
            "0"
          ],
          [
            "下",
            "1"
          ],
          [
            "左",
            "2"
          ],
          [
            "右",
            "3"
          ]
        ]
      },
      {
        "type": "field_number",
        "name": "angle",
        "value": 0,
        "min": 0,
        "max": 30
      }
    ],
    "previousStatement": null,
    "nextStatement": null,
    "colour": 50,
    "tooltip": "",
    "helpUrl": ""
  }
]);

Blockly.common.defineBlocksWithJsonArray([
  {
    "type": "turn",
    "message0": "向 %1 转： 旋转半径 %2 米，旋转角度 %3",
    "args0": [
      {
        "type": "field_dropdown",
        "name": "direction",
        "options": [
          [
            "左",
            "0"
          ],
          [
            "右",
            "1"
          ]
        ]
      },
      {
        "type": "field_number",
        "name": "distance",
        "value": 0,
        "min": 0,
        "max": 10
      },
      {
        "type": "field_angle",
        "name": "angle",
        "angle": 90
      }
    ],
    "previousStatement": null,
    "nextStatement": null,
    "colour": 300,
    "tooltip": "",
    "helpUrl": ""
  }
]);

Blockly.Python['go_straight'] = function(block) {
  var direction = block.getFieldValue('direction');
  var distance = block.getFieldValue('distance');
  // TODO: Assemble JavaScript into code variable.
  var code = 'witdog.go_straight(direction=' + direction + ', distance=' + distance +')\n';
  return code;
};

Blockly.Python['look'] = function(block) {
  var direction = block.getFieldValue('direction');
  var angle = block.getFieldValue('angle');
  // TODO: Assemble Python into code variable.
  var code = 'witdog.look(direction=' + direction + ', angle=' + angle + ')\n';
  return code;
};

Blockly.Python['turn'] = function(block) {
  var direction = block.getFieldValue('direction');
  var distance = block.getFieldValue('distance');
  var angle = block.getFieldValue('angle');
  // TODO: Assemble JavaScript into code variable.
  var code = 'witdog.turn(direction=' + direction + ', distance=' + distance + ', angle=' + angle +')\n';
  return code;
};