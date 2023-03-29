let currentButton;
var xmlHttp;

function handlePlay() {
  let code = Blockly.Python.workspaceToCode(Blockly.getMainWorkspace());
  download("code.py", code);
}

function loadWorkspace() {
  const workspace = Blockly.getMainWorkspace();
  if (currentButton) {
    Blockly.serialization.workspaces.load(currentButton, workspace);
  }
}

function saveWorkspace() {
  // Add code for saving the behavior of a button.
  currentButton = Blockly.serialization.workspaces.save(
    Blockly.getMainWorkspace());
}

function clearWorkspace() {
  const workspace = Blockly.getMainWorkspace();
  workspace.clear();
}

function download(filename, text) {
  var element = document.createElement('a');
  element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
  element.setAttribute('download', filename);

  element.style.display = 'none';
  document.body.appendChild(element);

  element.click();

  document.body.removeChild(element);
}