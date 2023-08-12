{ {
    _on_attach = <function 1>,
    attached_buffers = { true,
      [78] = true
    },
    cancel_request = <function 2>,
    commands = {},
    config = {
      autostart = true,
      capabilities = {
        textDocument = <1>{
          callHierarchy = {
            dynamicRegistration = false
          },
          codeAction = {
            codeActionLiteralSupport = {
              codeActionKind = {
                valueSet = { "", "quickfix", "refactor", "refactor.extract", "refactor.inline", "refactor.rewrite", "source", "source.organizeImports" }
              }
            },
            dataSupport = true,
            dynamicRegistration = false,
            isPreferredSupport = true,
            resolveSupport = {
              properties = { "edit" }
            }
          },
          completion = {
            completionItem = {
              commitCharactersSupport = true,
              deprecatedSupport = true,
              documentationFormat = { "markdown", "plaintext" },
              insertReplaceSupport = true,
              insertTextModeSupport = {
                valueSet = { 1, 2 }
              },
              labelDetailsSupport = true,
              preselectSupport = true,
              resolveSupport = {
                properties = { "documentation", "detail", "additionalTextEdits", "sortText", "filterText", "insertText", "textEdit", "insertTextFormat", "insertTextMode" }
              },
              snippetSupport = true,
              tagSupport = {
                valueSet = { 1 }
              }
            },
            completionItemKind = {
              valueSet = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25 }
            },
            completionList = {
              itemDefaults = { "commitCharacters", "editRange", "insertTextFormat", "insertTextMode", "data" }
            },
            contextSupport = true,
            dynamicRegistration = false,
            insertTextMode = 1
          },
          declaration = {
            linkSupport = true
          },
          definition = {
            linkSupport = true
          },
          documentHighlight = {
            dynamicRegistration = false
          },
          documentSymbol = {
            dynamicRegistration = false,
            hierarchicalDocumentSymbolSupport = true,
            symbolKind = {
              valueSet = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26 }
            }
          },
          hover = {
            contentFormat = { "markdown", "plaintext" },
            dynamicRegistration = false
          },
          implementation = {
            linkSupport = true
          },
          publishDiagnostics = {
            relatedInformation = true,
            tagSupport = {
              valueSet = { 1, 2 }
            }
          },
          references = {
            dynamicRegistration = false
          },
          rename = {
            dynamicRegistration = false,
            prepareSupport = true
          },
          semanticTokens = {
            augmentsSyntaxTokens = true,
            dynamicRegistration = false,
            formats = { "relative" },
            multilineTokenSupport = false,
            overlappingTokenSupport = true,
            requests = {
              full = {
                delta = true
              },
              range = false
            },
            serverCancelSupport = false,
            tokenModifiers = { "declaration", "definition", "readonly", "static", "deprecated", "abstract", "async", "modification", "documentation", "defaultLibrary" },
            tokenTypes = { "namespace", "type", "class", "enum", "interface", "struct", "typeParameter", "parameter", "variable", "property", "enumMember", "event", "function", "method", "macro", "keyword", "modifier", "comment", "string", "number", "regexp", "operator", "decorator" }
          },
          signatureHelp = {
            dynamicRegistration = false,
            signatureInformation = {
              activeParameterSupport = true,
              documentationFormat = { "markdown", "plaintext" },
              parameterInformation = {
                labelOffsetSupport = true
              }
            }
          },
          synchronization = {
            didSave = true,
            dynamicRegistration = false,
            willSave = true,
            willSaveWaitUntil = true
          },
          typeDefinition = {
            linkSupport = true
          }
        },
        window = <2>{
          showDocument = {
            support = true
          },
          showMessage = {
            messageActionItem = {
              additionalPropertiesSupport = false
            }
          },
          workDoneProgress = true
        },
        workspace = {
          applyEdit = true,
          configuration = true,
          didChangeWatchedFiles = <3>{
            dynamicRegistration = false,
            relativePatternSupport = true
          },
          semanticTokens = <4>{
            refreshSupport = true
          },
          symbol = <5>{
            dynamicRegistration = false,
            hierarchicalWorkspaceSymbolSupport = true,
            symbolKind = {
              valueSet = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26 }
            }
          },
          workspaceEdit = <6>{
            resourceOperations = { "rename", "create", "delete" }
          },
          workspaceFolders = true
        }
      },
      cmd = { "C:\\Users\\noahm\\AppData\\Local\\Programs\\Python\\Python311\\Scripts\\pylsp.EXE" },
      cmd_cwd = "C:/Users/noahm/DocumentsNb/BA3/Algo-TPs",
      filetypes = { "python" },
      flags = {},
      get_language_id = <function 3>,
      handlers = <7>{},
      init_options = <8>vim.empty_dict(),
      log_level = 2,
      message_level = 2,
      name = "pylsp",
      on_attach = <function 4>,
      on_exit = <function 5>,
      on_init = <function 6>,
      root_dir = "C:/Users/noahm/DocumentsNb/BA3/Algo-TPs",
      settings = {
        pylsp = {
          plugins = {
            pycodestyle = {
              ignore = { "E301", "E302", "E303", "E501", "E211", "E401", "E701", "E741", "W293", "C0103", "C111", "C112", "C114", "C115", "C116", "C301", "C302", "C303", "C321", "C326", "C330", "C411", "C413", "R022", "W391", "W105", "W611", "W621", "W622", "W401", "R0903", "R1710" }
            }
          }
        }
      },
      single_file_support = true,
      workspace_folders = <9>{ {
          name = "C:/Users/noahm/DocumentsNb/BA3/Algo-TPs",
          uri = "file:///C:/Users/noahm/DocumentsNb/BA3/Algo-TPs"
        } },
      <metatable> = <10>{
        __tostring = <function 7>
      }
    },
    handlers = <table 7>,
    id = 1,
    initialized = true,
    is_stopped = <function 8>,
    messages = {
      messages = {},
      name = "pylsp",
      progress = {
        ["003ac647-02a6-41d8-a3ca-285145808051"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["004f161f-65be-41c4-95d9-5bcb7d3b1d58"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["005a9050-cb5d-4e5f-bf2d-69b60e83bff0"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["0079a0ea-3ec2-4408-a627-c7692fa62b53"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["00b12126-2bde-44a7-a141-cd0e2c8ff948"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["012c10f9-c1fe-4320-9bf3-fb8303261198"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["01adde78-1504-46c2-8de7-3de9670353e5"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["01c9662b-781f-4647-acb2-da5ed9459d65"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["020e20e0-a350-40a7-aef3-3a7f992b943d"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["02412102-b8ec-4344-87af-1560872bac6e"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["036012fb-f81c-4b01-bbdc-ebb1884e82f4"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["036a1ba8-0a3c-4f9c-b202-a6786510e71e"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["03bb996f-e76f-42a3-9826-f56a9da31f20"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["04096e58-dd2f-44fe-a26f-e52fc4973637"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["040b4fae-85c9-4c28-843e-4f537c69f67d"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["050f7002-3c35-4f3a-9fb8-7f1570bdcc08"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["06085353-4e62-4c00-9684-6d7b706416b6"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["068694e0-c99f-4216-a4fc-6370f9029de6"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["06b8d8dc-b763-4804-9fb4-6377347f715b"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["06e132fb-531e-474e-bfbf-e6c4e362c7d0"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["07027fbc-5a80-458b-92da-ebac0b8fd977"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["070786a1-7e4b-45a4-aa69-ec20d18f9958"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["075f07e8-765e-423d-bf98-6bcf2762f8f4"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["096ec27b-8974-40d9-9f3c-353af01122ae"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["09e3230d-b9a0-483d-8c6c-11feccf48863"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["0a64a43e-dfd0-494a-901e-c2d0eb538ab2"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["0cbd4851-d344-4457-839c-869907b17863"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["0cecf151-d822-4806-ab9c-be517c60d57f"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["0d9788da-ac2a-450e-bdbd-53a234682f88"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["0df2f1ed-cac8-4e3a-92c3-2e3a289fa063"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["0f5e9213-8254-4920-b1c3-3c99e4861f87"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["0f895721-5d6c-4ea4-b976-c9c568d4b36c"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["0fda0d51-86ff-4506-a7ec-a18089e17716"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["0ff39132-9322-43e2-9286-20536c32b109"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["102d4bdf-6b42-4827-85d0-23d6b9b76744"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["109933f4-587d-40ba-b78a-1354e8f9a045"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["10fa29ac-9082-4280-b2fa-653b5f0e59f2"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["1162e45f-b3fb-4c02-986f-e4de43894a2b"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["117c556a-fbcd-4031-8542-303610ccabd7"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["119e7f39-6d1c-412d-84e0-9a258e3d06b5"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["11d17fbf-d31a-4be5-854f-533686bd8c7e"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["1209a766-bb4e-4f0a-94da-1fd4a1786065"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["126151ce-ce63-4481-9dc1-13ad4157ba16"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["1282e868-2e46-4001-9603-5fc61a3132aa"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["12876508-a5f9-45c0-a942-36ebf1f68993"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["13084a6e-fb82-4710-b07b-489dc7a1c3b7"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["132bc30b-3e2f-49a8-90d2-dc01f0125e19"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["1336e1a3-a6bd-405a-97f4-c2875ad182e3"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["137ca6a5-1a9e-4a4c-865f-7cda013df8a6"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["1416e1de-c55e-4d48-860a-0abcfdb1b0aa"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["143bf05e-cb47-440a-be35-3c0c11dd45cb"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["14799e92-982d-4730-bdbc-5dc77765d656"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["149fbd41-cc1b-48da-bc86-bafd0264818d"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["1508b8fb-9e8b-457f-bff5-a27053f98aa6"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["1572bd45-4a9c-4e3b-9c7c-91fb62770103"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["1743dc85-02cc-4b0d-b25e-03a5b08d04ef"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["1756f5d9-6ab1-4be8-94b6-f9f4a5d5afc4"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["175e6841-69cc-4a1e-b1dc-af4dc3ab82b8"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["17f33c26-c140-4d7c-a3e0-51ef8311e1d4"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["18bf8363-ac5c-44c9-b502-8673f5830ee8"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["1923a8ce-b904-4dea-b567-09c03f63e222"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["198693f4-8249-48a7-aa2c-b89643f45e71"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["1991a13a-1e32-499a-a6ce-04e5f92b487c"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["1ad0fae6-c7c2-4f39-a6d4-891f207fe23f"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["1cd2208f-6f1d-4729-88a3-741e5d664c3b"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["1d24b18f-9624-4ff5-83c1-334c76150bd1"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["1d46125c-9b04-4429-911e-b3aa59fc90b7"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["1d8713a6-753c-4ba9-a5eb-8c000610ca77"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["1da10d46-add1-438b-8173-08ce988d0003"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["1dca60d5-7978-4bdd-94c5-608bd31aeb99"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["1de3e8c8-451a-4a34-9c40-dd346d94849b"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["1df13e74-8ef2-41f8-8de0-e8cc73f24f5a"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["1e3531e8-a3f0-48d9-a867-389f07236ad5"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["1e908cc8-68d3-4078-83f0-94b37db30dd7"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["1f4f6a04-de4e-4afb-bd05-6280edd432c8"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["1fecd5e4-3fd9-419d-9169-5981a8e124eb"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["2042fa5d-08a0-46d2-b521-24456d29723c"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["207a7cdf-df09-440e-92f8-cbb85e785d76"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["20cdec5c-c79f-4802-b8dc-80303d4da6c7"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["22bcef11-e419-46c3-b918-c2051e12a875"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["23550277-03e9-437f-a17a-ec58d104d10a"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["23f25f4f-aabe-4f1d-ad01-fe3f2dd7c5eb"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["24945376-ea36-463a-927c-dc4706a57858"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["2494f832-5223-4834-a175-9317b4799dbc"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["24f7b2f7-e50f-49af-8355-64c1fd463c45"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["2509be40-9141-4b35-8956-08c27e45fca2"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["25e4472c-8866-43f9-a451-a04f1f32478f"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["262dd8b9-d48b-4522-9a52-42cf79d0b485"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["26c19ce2-81b9-43ec-9620-a8e47f744251"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["26e09186-6adc-438d-a3be-29e5f50ff5ba"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["26e7c77b-df51-449c-81c9-e8eb172d417f"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["27402ed6-5521-460f-ab04-0600048b5da0"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["28172fe7-40ef-462f-956b-ab52b45a3b1c"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["284090a3-0b02-43d2-b605-b22f6336c590"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["289de403-1867-4e42-acf8-8e8ce88f68cf"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["299c1b67-a7ad-45b9-b97e-217800543ded"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["29e2474e-d624-4813-ade8-c48e559bd6b8"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["2a276e03-1185-4a1e-8d19-01ee1926cdca"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["2a29f2e2-71a7-4f85-a807-4c02c283fcdd"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["2aaf8298-a169-403b-8dc0-9560755120ae"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["2aeef4f6-7329-4b66-92c4-51a00f60e149"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["2b475cae-04dc-491b-9f46-4ecd555f8728"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["2b836a82-219b-46be-8710-579664604b2e"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["2b981b9b-1e12-4a92-af63-262c49502fee"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["2b9cbe64-d717-47a8-9f71-852ccfc228fd"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["2baa3c69-0fea-4c4f-83a6-e96f40c1b290"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["2bb1b983-d16d-4043-8c50-b4819d5f8b0a"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["2c07ec10-b1af-4de4-b4b4-fb22cc6f8025"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["2d742dfb-29e6-404c-a23f-6878dcdda815"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["2daf4322-aa12-4e39-a379-810d9ce6af0f"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["2e250d18-8017-444f-b832-dec90859e493"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["2e2bf73e-8631-4544-bc8a-51befcc6ec89"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["2e55a688-221d-42c9-a9f7-d31e135a4c38"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["2f77f58f-6f22-4122-a90b-8270828f0591"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["30d541ad-1422-41fc-b052-c608e9b6a858"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["319156d7-d01a-488d-b243-30a278cb701b"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["31df14fb-dc66-48ea-a98e-38679ff1d296"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["31e5f34d-22fd-4a21-962c-e474c6522a09"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["327609f1-5214-42ab-a804-83fe03a13d98"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["329e7963-445e-4f29-9fcc-0b2b05c41c1b"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["338ea6d5-58f4-410b-8950-840e8bf827b4"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["342b1c64-5ee7-4073-8244-a384a636be0e"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["362961f7-0aca-428c-a05b-b3390405e8dc"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["3678c343-3b45-4673-816e-504d59be5c11"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["369bcebd-a003-4dca-9b8e-062e00fcda62"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["36b322ec-b9c1-44e9-b355-98359cde0898"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["38baf867-74f8-4164-99a6-6f342ea93bae"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["3956e49e-0f07-41b8-8369-44743024e584"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["398704cc-f102-4290-b8b0-a8d99d9b1edc"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["39894ae2-ec13-4a89-a368-5cf77d91b680"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["39c97742-c962-40e1-80b1-3f04349ce6ec"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["3a0a8640-ca19-4394-bc22-3f6ae38674fd"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["3a1ef843-0321-4d01-b975-35e609779b5f"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["3aba5f34-188e-4c67-9187-892e9aaf8081"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["3b1e3e16-ea94-4663-b412-10034a72d72b"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["3b3d3ee8-8427-4131-92d4-6d75c371f935"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["3c318620-01e7-468a-991b-a668d1dab85e"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["3dc809cd-7eb2-4b22-b5d6-dd4008882b97"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["3ea47b58-75fa-4a3b-ba5b-72ee565c43c1"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["3ec7c4e0-9c65-4573-9786-b6d428a3b52b"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["3f121977-00a0-4df3-8745-6d14542707e2"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["3f95ff55-c55d-435b-9de6-eadeee17a9bf"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["4001fadc-85d9-43c2-8798-55a4ec4bea4c"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["400c89ed-c13c-4a25-a72f-1044e04b0f59"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["40625f26-f203-4161-b481-3f2f81869aa9"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["406e6449-beba-41af-8883-1a60d4d09f88"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["40fa3d80-ae2c-4cd8-ac23-a7fb26c2e664"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["418e56f9-116a-487e-aa60-fdef7efe39c1"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["41b1a987-abd0-4590-9e7c-b8a520f5e427"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["430c3a42-3ac3-4882-a02a-0d070d55986e"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["43fe5705-93d4-4357-b0e1-67f2d6b245c9"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["441c065e-57f2-4825-a15a-dbb3d864c246"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["443de6b0-8b0b-445d-921e-d31751d00eb4"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["448e0e00-95c5-482a-9873-a0cab7b9eb7d"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["44ccea00-2c70-4ffc-b04a-249b358c920b"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["45c47a46-95f0-4395-be69-68c0055ae2cf"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["464834ce-7d0e-4b4d-97c2-84c1f182d625"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["465530c1-4bf5-4305-be78-8125baacc999"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["466aea70-85c9-4806-b0c8-acd31d699f65"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["472627b2-753c-48d4-b02b-9baea76a27a8"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["478d7e66-400a-4683-89cb-0843952db8a4"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["484e3fe6-90f3-4fa7-b3d0-5d43e88835ca"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["48859838-6dfb-44cb-bea7-808b66ab3477"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["49bd67e2-ff4a-4a51-8d01-1b4f7e1ccdc0"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["4a717650-25e5-4345-928b-595b295f36d8"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["4aa70fda-989a-4310-ae66-910632b98665"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["4abf83ae-9ffa-470e-8e7b-23ef7ee1d821"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["4ac3ffd9-f820-4fdc-bfe4-462628a7dc6f"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["4b1ba321-4751-4d65-bad3-4ea07b6b4e1e"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["4cec7362-d6c3-4433-8af7-9746e1eb7e2e"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["4d37f0e5-9587-4e52-8e1e-36d25b5da7e0"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["4d548073-baea-4625-8817-c9eed29647c3"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["4d6b9b69-cded-46ea-baf1-48a14ceadb60"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["4dfcb714-d2e3-4ad4-a472-145962b83a0c"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["4f37a305-b234-4625-9fce-7c49247e6362"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["4f40203c-61f6-413a-8bad-f9928df705fc"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["4f49e86c-4a3d-405a-aad7-597913d963a5"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["4f527260-96a0-46a5-868f-5f11614d4f43"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["4f691286-8ca6-4809-a55f-0b1f08cce31b"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["4f750d8e-51ca-48a7-84ab-c7954442f885"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["4f9311c8-55f9-43c4-8979-827fc7f4fc01"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["5037377e-b413-48e1-8d8d-b24d5ead7684"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["507af46c-2582-491d-a1a8-a3259f4de086"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["531bd945-bacb-4dfb-9779-a9c5c8873bed"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["5326b970-ced9-4246-8ada-d0e8faf7647b"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["5427d336-be36-4ebf-b87c-ea2db1f336e5"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["542eb0c3-3426-48c3-afd7-ab6f0d7155a4"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["543d78a4-12f0-4f3c-8192-7cc8ef502286"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["54e6a824-5931-455e-9a9e-c8ca4dbd09f5"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["55b0508f-36f9-49d1-8e88-9e0be6ea568c"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["56343106-37a2-4514-9f7d-2306017bcac0"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["56ac8606-b05d-4318-bba8-ebbf64b99d6b"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["56f27c45-92d4-46e1-b933-4d94997a735a"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["573dfec7-6f51-49fa-b38a-87e11e0cc4df"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["57a4e596-c3fe-4724-82d4-067e0c4958b8"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["58f0e2e1-f856-4304-900e-cec8108cd01c"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["58f8a3f6-e131-4f3e-865d-6e144e765cb1"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["5900a762-4f84-4558-be3a-2557f30dc37e"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["591067d7-bde2-4f8b-8027-d4f728484975"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["594b4707-181b-479e-8e1f-7c116ea0f3b1"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["59ab1ff7-71f4-4ec3-bab2-2e232ceaa1b9"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["5b0d4c09-9ce3-4598-95ca-cb93c9b897ce"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["5b564357-68b8-44dc-8616-c71bab0a7d67"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["5bebc8ac-9121-489a-a6a8-f2b700de3ead"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["5c17214d-7d22-4da7-9fd2-62f1bc4e07f2"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["5d792486-fc90-4c14-9a44-2261f3ca27a6"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["5ec4914e-912e-4360-8901-30bdea05ac3c"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["5f3f7ec0-6db1-4ff4-9354-6a2a1716de97"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["5f87f7bd-3b1c-4b9c-a4e0-c0ab941368b9"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["6082f643-9ce8-4299-8097-693358e2112d"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["612bac03-712f-4350-8700-4621f138d64f"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["61429309-ed5c-4c18-a2f8-6cbda4fa2b7b"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["614424eb-10be-48ee-baaa-f1ddbc8c09b7"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["61641bc5-d1e3-4264-b495-5be6091a0d1e"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["6219e144-34e6-4962-ae23-d26a528de541"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["62373e8d-f0cb-467b-ac72-e85f6fbaee7f"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["6254207e-fe79-493c-83eb-a034d6c05060"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["62d5f4a1-96ac-4a3f-93a1-2e1aa8a59aef"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["644e1a0c-b0c3-4a38-b432-68d8d5a5bdf0"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["645618cf-df19-48bf-89dc-b94c6b669851"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["645fc3ca-2abe-4fb5-921c-37f87af30c62"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["64d28c66-d0f7-4cf3-b7bb-c1efe29c4310"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["6508b121-aa0d-4b0d-93c3-c4dafceed55a"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["656d70aa-9662-4312-91a9-cd4fd503160f"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["657d9911-2707-42e8-a533-76ecaa8633e3"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["6583b62c-dc52-454e-bc4b-b15662c592d5"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["67056551-1ae8-434a-9371-cc69e136f083"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["67c9838e-493c-411b-8171-85a0c6f3a52d"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["6816918a-15a8-46fa-83d1-8b54b35d314d"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["681ae5e0-414e-404c-a131-e1fddb1441ec"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["683e2ffe-c90d-4658-bdcc-3d3d6c7f36b5"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["69236376-8001-4de3-90a9-0db020b2a108"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["6933e82e-9927-4955-8b56-e2eeca60b74b"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["69a44064-eb86-4586-8e93-9878a13afd54"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["69c46c2f-c0c6-4525-978d-a9dbf8f8a5ae"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["6a57746d-86ab-4263-bfae-1623275c6737"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["6bcf85b1-8614-4d38-a949-b6bfa5a55c17"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["6c70c23a-25a7-4e5a-8e9f-ba0d2354155f"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["6cb674b7-5c7a-42fd-be25-888062569b1d"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["6cd155a7-0b30-4bd8-8b56-77e01161ab8d"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["6eff0b7e-54fc-4fed-88ed-31b5390fa2d7"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["70390cf1-0d68-4a75-945a-4d3b339f1c92"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["7115184a-974f-4fbf-8e75-c00da5423591"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["71688019-81f3-4d17-a00f-0e21181b2f9f"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["7257afa7-dde6-499d-aa97-e7005403a86d"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["72b48ee7-a2fc-4974-94ba-53510062ba4f"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["72fe1f3a-3a5e-4508-8a1b-8afa4cf46bc3"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["735bf383-5476-4fb7-ba58-5cf3f9d1049f"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["73ca69c7-2ebf-4dca-9bf8-576951c620ee"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["73cb3e50-ecf2-4bb4-b489-39ad2966a43f"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["740434dc-8608-4e43-ae46-da85e4c633a4"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["75d598a4-9ae9-481d-972d-e4b0a392bbf9"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["75fa8701-edb2-4674-a2e1-b2acd8b5a750"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["76cbe4b6-a907-4773-89ea-4381483ecc8b"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["77736519-03ad-4153-8870-73da8890f4fe"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["77831134-e6b6-4c66-9623-ea5e7d485f53"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["781bfe55-eb4f-4ea4-93ad-193989738f7e"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["784527a8-e6de-4561-925a-c8ec49ecccbe"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["786454d8-88da-4aa7-8d13-0c11610b79bf"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["7a12a9a6-0b68-48a8-a431-2b4d9c0da1bd"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["7a1466cd-4658-4da6-961e-84720474f4cd"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["7b0663f7-d2cb-43f5-b83c-e9a9edb5a82d"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["7ba72877-ea94-46a5-82b1-64767e3b62b2"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["7c3348fb-2374-4cca-ac11-28a6beaffd1a"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["7c6f41cc-0e4d-4afe-9953-fe8a49bebdc6"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["7cc5b969-4fa9-4139-acde-2313ee71f524"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["7d5af2f2-7291-44e1-a160-70064d112afb"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["7dce9005-49d0-436b-b4a8-c5bfed162150"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["7fc7d793-0cb7-4f33-87b6-f5edb84ff96b"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["808770a2-48b8-40a4-a18d-4dcce3126317"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["80cb0719-d1da-44b7-a1bd-16df6f4841eb"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["81f15802-1f19-4ef5-b9ae-8fb7b453b9e5"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["82d32662-e074-4b64-85f9-c0ad6837e816"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["834f4673-9491-442a-9959-f1758fbda7a5"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["834fcfd8-c5b7-492a-9dcf-cdd4cabe3b02"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["836688a7-a251-440e-8b71-7984b1788e77"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["8392be74-ccdc-4f24-9299-e68868382878"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["83df40dd-837f-42ed-b878-d2d296482f12"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["83f7aa10-a9d5-414d-9f18-1c3f7014dc6e"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["844ce675-a34e-4a64-84c9-5b6d834e63e6"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["84d23a60-6535-4534-ad33-4deda3854478"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["85d0293c-7ffc-4a98-b2a1-b17143ce75e7"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["86a96d31-0828-47c9-9d6c-911185201267"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["8799859c-6faa-4ad9-aef1-7a525122a590"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["87adfed8-745e-41e2-8ed6-59ca32e905a0"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["87fc0cf6-0b11-4d4b-a415-a27dd37c3494"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["88a3e683-da66-4fb0-a5f8-0d3d01151959"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["88af74bd-00d5-45cd-9ed4-dd8730e4384a"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["88df3d66-06f2-4bdd-9e6e-d25f5ff64e58"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["88fc3075-7573-4142-b599-19b1999f0aff"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["892f9c93-43f7-4561-b124-bd4f8357b7f2"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["89cdaf08-6728-4393-b59b-18a57c507ba9"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["89ce9c12-f834-471a-88a0-dcd576d65f32"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["8a9dd655-f460-4fb2-b788-96b3bd6bc989"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["8b032d2e-ff44-41d4-950a-66090563ea75"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["8b16bfba-be0b-4572-9a26-6d1890c7f2d3"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["8b5f3a5b-ff97-4025-9241-c382964facb3"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["8c11d89b-0652-4997-96c6-9a75e03c27c7"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["8c47b838-2580-44a5-bdb8-670e18e3affb"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["8d24bff3-4743-46e2-93a0-7a22ab58fe28"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["8f8a6d6f-bf23-494f-9ba6-7c1b427270ec"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["9028bb1f-83dc-48b7-ac5f-79cb12592d1e"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["90d3400b-2025-4a22-8742-442d70f71e15"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["91543505-85bf-45c0-be14-c732bbc8c35a"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["920e8c1f-838e-4ba6-ad06-96a337d4d346"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["926e0749-d26e-4229-bdb3-e835f1948fa5"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["9272d9fc-a086-4606-a3db-3c4da4ac15c5"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["92765e24-de95-493c-8815-c7df736ffdf9"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["9277ec97-9058-4ae1-a99e-dc3d5cc1d5c8"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["929563b4-db7d-487d-b025-eb16dc6dcec3"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["92a34cdb-8c05-4a78-86fd-acc55a2b29be"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["931c881c-ce67-4196-8848-d304911e9332"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["938d8b90-a405-4033-90bf-fa88457c1a66"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["939047fc-9832-4e69-8602-4c7906d88cfc"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["93bab5f9-cdc3-4347-ac47-a16c955ff0ba"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["93eec41e-fcda-42d4-a71e-424bf06473b4"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["9423ca12-673d-4a5b-a802-bc0d079edd5f"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["944de5de-4ad4-4792-9ec8-28b03e65f6d7"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["946b923c-b2b2-45cf-ae22-64d27b30e023"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["946f9e8c-94fd-4341-af93-5ea919338a30"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["953c3613-bd5f-4bdd-af95-610e723ae968"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["953ec159-a6e3-429e-80f4-20f6dcf7f737"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["954b4717-2323-4798-9c05-b702f2ecc4c3"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["954f3f47-6876-44ac-98f7-0ca323973c17"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["95e23e81-80ab-4cf7-8cc2-2d5ae63a9a2d"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["96566e49-6ecc-4995-bd15-e2fedf7ee7a7"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["9660366b-aea5-443d-ac2b-e29b3d72fd83"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["9799cbcf-e71a-49c7-b1f4-86e5a332bb68"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["97aa2174-7e1b-4540-93c4-58e6ebfb5775"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["97f6390c-70e9-4dc0-9742-feec0f36081f"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["9843a636-abb3-4ff5-af6e-528e88d7950c"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["98488ad3-dcbc-465d-9ae4-7c9d6bf3483b"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["985cd74a-b545-4c10-a5f7-09a7c6d1926a"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["9879f42c-0d59-4afb-8c37-12f51fe50415"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["992b08a4-07fa-4257-8b78-15969e4507ab"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["99a0933c-67cd-452f-9854-a92f37927b16"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["99d3e5b2-57f3-46db-ad0f-0d9657191671"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["9b2fbb57-5d49-4742-b003-5ad89dc58dd2"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["9b7547d7-21f6-4496-8525-31f8d63f3f0b"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["9c2fd776-d8e8-471c-b781-b5dcf5880946"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["9d122b9c-35a7-496a-a8c1-2654ebd2b44f"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["9d13714c-5ed0-49fa-b7ae-1f882d08b73a"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["9d862cc1-4036-4a5e-9eef-99a8a25ce87f"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["9da46361-7cd2-424a-90ae-83b2fbffa620"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["9ecb6d08-2214-42e5-b467-bd4d59214fcc"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["9f20b044-1e21-44d6-a699-4d20ff6cae57"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["9fa3f462-3bb1-4f37-b9ee-7b55fd050ebf"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["9fc9e44c-1257-4e17-81dc-35e747674ad4"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["a103f4fe-1ced-4920-b798-d70160882964"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["a10dd4da-587b-4fb3-a502-e3b3b5cf8d35"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["a1c5cb6d-2876-4ef5-91ea-404f05e12ff1"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["a1e6b0ea-6397-44a4-8982-05785f72a57f"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["a2ced439-bafd-4cf7-9ab0-4b191823f28a"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["a30c9594-e311-4609-8ce9-284268d195be"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["a35e3f8b-1181-4a01-a3d4-c24cff118317"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["a3976252-7947-48f1-92fe-ce031fe0df76"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["a3fa3848-3a62-4980-90ed-a45b57b8fbca"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["a49103d1-81ef-4c5f-9ba8-ec5633c631a9"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["a51be03d-f09d-4155-b6bd-7aa896156c30"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["a58ce8a8-8238-4716-b84a-faecb3b47aae"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["a592a53a-da67-4fe7-9a32-e993cefe1197"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["a59994f4-719e-424c-88e9-4940270863b6"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["a5f452a6-999c-4e6c-b509-ae85bbf60ec5"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["a62d3123-2436-4e8d-be07-6c85f7e4253a"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["a698b4c5-f4a6-4cf5-8b0c-64b7c5067982"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["a6cc59a6-7fd4-4195-a4d7-03c9fb8486c5"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["a7c48646-4b1f-4f54-ade4-9c55b76304a2"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["a7ca239c-0253-46c2-819f-ad7501edc9ae"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["a82e09c0-95fb-4395-9b67-310e38f15013"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["a84862c2-664f-49b2-ada7-42171105295a"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["a8c61bf8-7a80-4493-a143-b5402e170c5b"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["a98eb38e-cd5e-44d4-8636-9015e52a5acb"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["a9acd4ea-66c4-4a3a-ad15-578e24d79300"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["a9e28e42-cecd-4e56-8671-51350224193a"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["aa61b192-71f3-4138-9dc8-7f21db19c410"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["aac8d142-6a3f-40aa-9442-4eaea92df583"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["aaebb264-ff03-42e3-b5d1-3b23595f9f6b"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["ab2e3d2f-dd42-4749-a032-0ffc0899b531"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["ab727072-5939-4214-be5b-a76db8dd1cec"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["ab82228a-5b2b-4d59-87ff-a385b7304d3f"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["abb0041c-b86a-4329-9b31-bfb6cd933c92"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["ac59c543-43a9-4cae-973a-099af65fb59f"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["acff109e-f833-4647-aaef-c55a90e943c8"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["ad3f3988-61ec-4fa1-a84c-92c70b8e1f2d"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["ade22651-eef7-4a06-8fe4-91b8c25e034b"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["af1df55c-f92d-4150-b9a3-09b52a730f1f"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["af9d81cd-3352-4c8b-839c-e9afa86044c3"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["afe3693f-6fd0-4d3c-b7cf-ce75ee156b93"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["b04514b1-2860-49e4-b1e2-4c3901eeb3b8"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["b09831aa-f15d-491d-900c-87ab74e1c851"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["b0ee5dd7-ebfb-4660-b8d3-9dcd13892621"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["b0fdde1f-1425-440c-bdb0-175af21af265"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["b1433cc2-d207-4504-862d-b03eb8564c69"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["b1d2a598-2f24-44ae-bfdf-b27957691e93"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["b1d9ba49-2b11-42d2-9571-6677d97f585a"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["b288282e-be79-4daa-b24c-9d643eaea00b"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["b51ee707-3a4c-41c2-a706-1b77f8890042"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["b5202fc5-5590-44eb-853c-3f16228be92d"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["b56511b1-2cd2-495c-b121-95313daf36aa"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["b5927ef4-bd22-46f9-97ac-cd4e0d4b654e"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["b62d3dc2-722f-47e8-9975-9b80363d55e9"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["b6a670b4-8252-488c-bb2c-2d5f99e5d2db"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["b6b4802b-86bd-4578-93b6-9e6828324831"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["b6bb15fd-5eca-4319-bf21-ba4306f3fbc4"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["b77cb81a-354d-4668-b8c9-6dc65fcee3a6"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["b78195ba-c4e2-4f06-b0da-84f12b8be76e"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["b7b123d8-c154-409e-98df-0e908ee5b0fb"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["b809216f-74e6-44f0-9939-bf37db4cefbb"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["b8d0c8db-1013-4308-80b4-73deedfa3d3c"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["b8f53307-255f-4aac-abde-9948238b77f2"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["b8f831d3-a743-438c-8c5b-d3e71763cdcd"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["b92ef450-5033-4f56-917b-69048e68611a"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["b98942af-9f14-41fe-97de-b698a3b665e2"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["b99b6364-5836-4062-a041-466a1d3e68c5"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["ba424802-8b96-48b9-a48b-0f5c90843233"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["ba48cf26-7192-4791-aa06-964fdb4619f4"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["ba4f8f8b-1550-4ccf-994f-ec109d321890"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["bb6e20ae-c2ad-43bb-b973-620e7b916400"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["bbc54663-b56e-4191-97a1-603d2d6accac"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["bcad29ce-6d81-4329-904e-4f230011f447"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["bcc11b64-af1c-4324-bff3-8b7cd2bacdc1"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["bd673ea8-96b7-4b1e-b767-a44a854aa7bf"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["be3d3508-44a2-400e-900c-6f1ec7194f42"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["bea49f08-cfb1-461e-809a-82436c7a4c08"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["bf2a70d3-5e0e-47e0-b197-37c11cc04177"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["bf6eda85-d48b-4cf6-bc3f-9b97f07cb223"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["bf8e91b1-fc37-4f64-874a-63b4922ac167"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["bfcc20f1-04c4-4acb-8cda-19e9059deae6"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["c00691f0-1fd2-43d8-9cec-89c7397efe58"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["c09965ab-0980-4500-9e90-668d4f98c227"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["c196d5fe-7a82-412a-a272-7595b7621611"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["c1a2d2d2-3063-44ce-b682-351cc071b0e1"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["c1ac60f0-04c6-4c34-abc9-d9354cf5d4fe"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["c1b3b0cb-2c96-4db2-b3a1-d50e1ee2eb2d"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["c1e71e3e-85b8-4836-bf49-2253c71110a6"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["c1fda6f8-7416-439c-b9d2-5427b43d915d"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["c2179439-3a7b-454b-a596-e0031a088692"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["c254cc57-f6f0-49f0-8992-8e690f2b5fb7"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["c25e9f69-67d6-426e-84da-dddb0fc5578e"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["c274164a-362e-4713-97da-794d78f9831d"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["c2cb9b5d-2ec5-43a4-8b3e-aafcc409baa1"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["c3169607-3a43-424f-89af-9d14f1c272d2"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["c327e5fa-c311-4a0c-8271-626979d379e9"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["c385968f-3a36-419d-98b9-9dc56b7ebd4e"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["c3abc800-8836-49b4-9f35-c32f4947e5c4"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["c3d5267b-3a9e-4c52-be7e-7ef31e669c83"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["c3e15890-1479-42a5-8c4b-fcbebfceac7a"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["c423d399-9bc7-4726-b952-b317309e57ce"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["c481150d-e042-4d3a-8884-77ad3273679d"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["c4f85359-c2fe-499a-a89c-9d3bc77e07b9"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["c5543d27-33e5-4297-9643-7b5fdd6160bb"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["c59cfcf4-6219-49ce-a811-c4e5b788396d"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["c603c19c-e9cd-40a8-b6fe-9eddeb3feffa"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["c6892875-54a5-408b-b40a-a2b74bbe260a"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["c7673a53-ec35-4190-b0fd-83d1e10285ab"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["c7bc219f-167a-4a48-9b2f-1be1c2242864"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["c7dec4ff-6d2b-455b-8c77-ecd43b282643"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["c832a19b-20d4-43f9-9ea5-14d9967139fa"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["c8dbcc3d-5ee1-4db7-bc85-6118b56c178c"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["c9f2fb49-6ad9-4228-af32-e3c81b37a894"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["ca2db2ba-9ff3-488c-b045-a8617bd9eacc"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["caa0add5-7b2d-4d53-a088-a04b9661a112"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["cbbfa389-b8f0-47b4-a028-ac6fd8823eac"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["cbebdc95-aaaf-459f-8eba-d39ed989f7e1"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["ccc37b7b-35b4-4379-b172-7bda267ce1f6"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["cd24001f-5c9b-40ff-9a2c-9732c29feaf2"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["cdfc153b-ee93-45a8-a693-94cf2906be1c"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["ce506146-f412-4241-b015-fa054d4a2666"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["ceb51bc4-65c1-4fb3-bb72-8bb75b6b524f"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["cf604b40-7ade-49b8-91c6-3cc75928914e"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["cfad752a-f65e-4cc1-93db-5a903d675bd9"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["d04eea2d-c262-4cff-afcd-dd7b267e642f"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["d0522166-f976-4743-bfcb-c280f27f3408"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["d0d41386-2047-43d3-be21-4062dcaa2521"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["d0e229d2-f718-408b-ac65-cfa2cda126aa"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["d1a13f4c-9d7d-4143-8b87-905a5be6c162"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["d1b465b9-66bf-4a20-b1fe-2d9587bdbab8"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["d1cb8587-de9e-40c8-ac55-f54da757f87c"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["d285b70f-8af1-4cc8-9f2a-880d022017ab"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["d343d40f-cdfc-4f5f-be62-15d53429cce1"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["d4281d2a-8561-4f7d-bf4c-ce3c9053df4e"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["d546a64e-ecca-4c2f-b096-e08c7f81c9a4"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["d55e8126-e400-4ab6-b1ee-b0dce44174e2"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["d58e63e4-d0f2-47a5-9493-0089ddce20b3"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["d5ff08a8-3a6c-48ad-8a5c-66f76f094777"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["d6fd61ab-58f0-4c63-8bce-520c75f51a62"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["d7a81cec-ac98-41bd-9027-32d14b6036fa"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["d7ce9274-b759-4cc2-8093-6456c89c772a"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["d85ed6fa-3870-4268-a391-92b94be589bc"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["d86e811b-39ea-49f2-9ae6-407c249b385c"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["d8ec2277-3946-4488-9f43-242738fc9c05"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["da3ce6bf-ce09-4674-a61d-489b22ca9aa2"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["da815443-d1de-4940-8172-4b20f44331c2"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["db0c114c-b864-45a4-97e2-4ce2bcfca8f7"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["dbf87336-bb2f-4228-931b-77ba562e7513"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["dbfc66b5-3c69-472f-9d5d-7ff96582137c"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["dc193315-6284-4040-8767-85946d12d859"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["dc1da787-ff9e-4c85-9359-624f6acd9da6"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["dc32c49d-928a-49ca-a0ba-537c7d247b0e"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["dcb02179-e58f-4bb5-bc43-7db595ab1bda"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["dcffcf97-9809-4c27-a6c1-6b19edf183df"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["ddc28338-8ad9-4e10-b8e7-6c986a5c2a7d"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["deb5bfd4-9feb-4019-85e9-f204f1db7202"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["df93c188-b6cf-47e8-a232-3cd4dce41646"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["dfa32385-ca94-4212-86e3-d7dad1d09ca5"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["dff7bfba-e10b-4cef-a944-69cc9e6407bd"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["e0231404-bf4f-44be-a3c3-6c77ff7be5a6"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["e0b9a531-5550-44f1-be61-99dbfc353656"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["e12b2112-a9da-4078-b36e-0b37997b9ec8"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["e1bce886-0b56-42b7-810c-ed3a45c4a38a"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["e1e50824-929b-43a6-a30f-f5105e5a6e62"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["e1e963df-f57e-479c-909b-6f25b2b5ee07"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["e1ee2b35-ca92-47ad-8515-3fcd3a13b491"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["e2004b3a-d1b6-4fe3-8903-c873b490fc94"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["e21c5290-9120-47f9-a957-4bc2288b079e"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["e2b8b259-7c1a-47cf-aeb0-f07df6c97002"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["e313f665-a40f-4962-aea9-d416fff092df"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["e33f1d6f-65ac-43a5-9549-46609cc54aa1"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["e3b108a4-0b66-43af-b918-b9029c382bb8"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["e49768d0-53dc-4835-9ecb-30fe8c3768ec"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["e6dba371-cc58-4290-a93d-a873b36e1a7c"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["e6e571df-90b6-48ad-a09c-0b0b8245bcfd"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["e6fdf43f-78c5-4c53-bda0-45749d79e9ef"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["e866b139-cf81-4819-a317-e910953e8ffa"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["e8b6bccd-47aa-40af-af5e-79344f7f9d00"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["e93f4846-d002-42ed-8a37-4383712503fd"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["e9968962-45e1-4c41-8184-f7caeee407df"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["ea4cf1cd-df62-4d79-97e8-89c01f190376"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["eaddd46d-f893-4aad-9b73-8536220f069a"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["eb63f6f6-d99e-4578-8547-38fbb63b82d6"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["ebbe3474-3016-4cee-8d4d-8b5d793b654a"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["ec7498cc-ad33-41c4-a0d6-e633d37f006f"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["ecb65145-1b2b-4bfb-8d52-ec2463feae48"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["ecff7e80-10a5-40aa-902a-3c2aa058643b"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["ed5a8fb7-ddfb-42ca-911d-a74f32bdf93a"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["eed7922b-282c-4999-a065-8a5cc8babbc7"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["ef738b3c-8b7f-42c5-b642-ae4a61a08110"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["f05e4b99-2d1e-4ea7-8d9a-df8c59617dca"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["f12282a2-f47b-4827-bb3f-c39eff4bfe14"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["f12a3ef8-6cfd-47e7-9811-4324ded19a4a"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["f1575074-a2ae-48aa-9744-6e4f8cc6c109"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["f1dd1752-6ea3-412d-b84c-56b298bd07e6"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["f1e5da8e-083b-47a0-9f3f-9c851165cea0"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["f21bd3a2-9b1c-4fae-8ca8-12ef04d17513"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["f2f13a40-b835-47e4-af0d-ecf5ea861122"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["f3c940aa-4b17-41ba-b80c-afbf138f0e43"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["f4262d13-8283-45f7-ba75-d3cc86b347f2"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["f46804dc-9d6d-4374-9cf6-f9836f975482"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["f4800df3-6b4b-40e6-8435-4d20f3031cab"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["f53c7a92-8767-415c-a5aa-523259096eaf"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["f5762c44-56c5-42ca-ace6-431b357b56aa"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["f608930c-dc61-4313-aeec-5d57ca01f8de"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["f701ebf9-5e23-4647-9f54-f5b52e0a093c"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["f7f8e925-ccd2-4976-85ac-e2fbdcdd5fd6"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["f8433d11-c23a-4a8c-8bea-bf933772550a"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["f85481fb-57fc-4015-a819-eba5caa843c6"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["f8db3e66-dde1-405a-bc8f-7ef17449d0e2"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["f8e7fed3-9228-48dc-aa0a-7b7074c24dba"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["f957a583-57f7-4937-ba7a-5061d663bd74"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["f9a5a1f1-5ad6-4472-986c-00662f9ac2e5"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["fb7664e5-c6d7-4d53-8190-38cb6030ab6f"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["fba7e485-7da4-4d47-920f-e32c8a40308e"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["fbbb02c8-8135-4317-9ffe-1d2428b82d88"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["fbfd2b93-8118-45ad-bfdc-43464cc13135"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["fc8d9f2f-38c4-41f3-b4fa-e78b32d783c7"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["fcc843b8-0007-41d1-9153-64b3dbe40213"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["fd490823-3699-4184-94ca-6a5deb9579da"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["fde70adf-5f0b-4f8f-aab8-37c6f10d796a"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["fe1a16f1-3388-4925-89d9-2f1fa8a7c714"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["fe2b8492-1477-4821-9bfe-09d9bcc1729e"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["fe7526c9-a3b4-4bf1-a0c8-e2b2159d735f"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["ff1ee141-60ae-4fed-8968-ccc06626fa58"] = {
          done = true,
          title = "lint: mccabe"
        },
        ["ff54b4ec-51c0-412f-8391-a30629a94457"] = {
          done = true,
          title = "lint: mccabe"
        }
      },
      status = {}
    },
    name = "pylsp",
    notify = <function 9>,
    offset_encoding = "utf-16",
    request = <function 10>,
    request_sync = <function 11>,
    requests = {},
    rpc = {
      is_closing = <function 12>,
      notify = <function 13>,
      request = <function 14>,
      terminate = <function 15>
    },
    server_capabilities = {
      codeActionProvider = true,
      codeLensProvider = {
        resolveProvider = false
      },
      completionProvider = {
        resolveProvider = true,
        triggerCharacters = { "." }
      },
      definitionProvider = true,
      documentFormattingProvider = true,
      documentHighlightProvider = true,
      documentRangeFormattingProvider = true,
      documentSymbolProvider = true,
      executeCommandProvider = {
        commands = {}
      },
      experimental = vim.empty_dict(),
      foldingRangeProvider = true,
      hoverProvider = true,
      referencesProvider = true,
      renameProvider = true,
      signatureHelpProvider = {
        triggerCharacters = { "(", ",", "=" }
      },
      textDocumentSync = {
        change = 2,
        openClose = true,
        save = {
          includeText = true
        }
      },
      workspace = {
        workspaceFolders = {
          changeNotifications = true,
          supported = true
        }
      }
    },
    stop = <function 16>,
    supports_method = <function 17>,
    workspace_did_change_configuration = <function 18>,
    workspace_folders = <table 9>
  }, {
    _on_attach = <function 19>,
    attached_buffers = { true,
      [78] = true
    },
    cancel_request = <function 20>,
    commands = {},
    config = {
      autostart = true,
      capabilities = {
        textDocument = <table 1>,
        window = <table 2>,
        workspace = {
          applyEdit = true,
          configuration = true,
          didChangeWatchedFiles = <table 3>,
          semanticTokens = <table 4>,
          symbol = <table 5>,
          workspaceEdit = <table 6>,
          workspaceFolders = true
        }
      },
      cmd = { "C:\\Users\\noahm\\AppData\\Local\\nvim-data\\mason\\bin\\ruff-lsp.CMD" },
      cmd_cwd = "C:/Users/noahm/DocumentsNb/BA3/Algo-TPs/leetcode",
      filetypes = { "python" },
      flags = {},
      get_language_id = <function 21>,
      handlers = <table 7>,
      init_options = {
        settings = {
          args = { "--config=C:/Users/noahm/.config/pyproject.toml" }
        }
      },
      log_level = 2,
      message_level = 2,
      name = "ruff_lsp",
      on_attach = <function 22>,
      on_exit = <function 23>,
      on_init = <function 24>,
      settings = {},
      single_file_support = true,
      <metatable> = <table 10>
    },
    handlers = <table 7>,
    id = 2,
    initialized = true,
    is_stopped = <function 25>,
    messages = {
      messages = {},
      name = "ruff_lsp",
      progress = {},
      status = {}
    },
    name = "ruff_lsp",
    notify = <function 26>,
    offset_encoding = "utf-16",
    request = <function 27>,
    request_sync = <function 28>,
    requests = {},
    rpc = {
      is_closing = <function 29>,
      notify = <function 30>,
      request = <function 31>,
      terminate = <function 32>
    },
    server_capabilities = {
      codeActionProvider = {
        codeActionKinds = { "quickfix", "source.fixAll", "source.organizeImports", "source.fixAll.ruff", "source.organizeImports.ruff" },
        resolveProvider = true
      },
      executeCommandProvider = {
        commands = { "ruff.applyAutofix", "ruff.applyOrganizeImports" }
      },
      hoverProvider = true,
      textDocumentSync = {
        change = 2,
        openClose = true,
        save = true,
        willSave = false,
        willSaveWaitUntil = false
      },
      workspace = {
        fileOperations = vim.empty_dict(),
        workspaceFolders = {
          changeNotifications = true,
          supported = true
        }
      }
    },
    stop = <function 33>,
    supports_method = <function 34>,
    workspace_did_change_configuration = <function 35>
  }, {
    _on_attach = <function 36>,
    attached_buffers = { true,
      [78] = true
    },
    cancel_request = <function 37>,
    commands = {},
    config = {
      autostart = true,
      capabilities = {
        textDocument = <table 1>,
        window = <table 2>,
        workspace = {
          applyEdit = true,
          configuration = true,
          didChangeWatchedFiles = <table 3>,
          semanticTokens = <table 4>,
          symbol = <table 5>,
          workspaceEdit = <table 6>,
          workspaceFolders = true
        }
      },
      cmd = { "C:\\Users\\noahm\\AppData\\Local\\nvim-data\\mason\\bin\\sourcery.CMD", "lsp" },
      cmd_cwd = "C:/Users/noahm/DocumentsNb/BA3/Algo-TPs",
      filetypes = { "javascript", "javascriptreact", "python", "typescript", "typescriptreact" },
      flags = {},
      get_language_id = <function 38>,
      handlers = <table 7>,
      init_options = {
        editor_version = "vim",
        extension_version = "vim.lsp",
        token = "user_h9G64jjwOfnIWp1G58Si55CbpHsgieOtpKAmh49NG4pn_h1_9MOH3bCNiAA"
      },
      log_level = 2,
      message_level = 2,
      name = "sourcery",
      on_attach = <function 39>,
      on_exit = <function 40>,
      on_init = <function 41>,
      root_dir = "C:/Users/noahm/DocumentsNb/BA3/Algo-TPs",
      settings = vim.empty_dict(),
      single_file_support = true,
      workspace_folders = <11>{ {
          name = "C:/Users/noahm/DocumentsNb/BA3/Algo-TPs",
          uri = "file:///C:/Users/noahm/DocumentsNb/BA3/Algo-TPs"
        } },
      <metatable> = <table 10>
    },
    handlers = <table 7>,
    id = 3,
    initialized = true,
    is_stopped = <function 42>,
    messages = {
      messages = {},
      name = "sourcery",
      progress = {},
      status = {}
    },
    name = "sourcery",
    notify = <function 43>,
    offset_encoding = "utf-16",
    request = <function 44>,
    request_sync = <function 45>,
    requests = {},
    rpc = {
      is_closing = <function 46>,
      notify = <function 47>,
      request = <function 48>,
      terminate = <function 49>
    },
    server_capabilities = {
      codeActionProvider = true,
      codeLensProvider = false,
      executeCommandProvider = {
        commands = { "sourcery.login", "sourcery.login.choose", "sourcery.effects.set_enabled", "refactoring/accept", "refactoring/skip_one", "refactoring/scan", "sourcery/rule/scan", "clone/scan", "clone/resolve", "refactoring/skip_forever", "refactoring/skip_version", "config/create", "config/rule/create", "sourcery.openHub", "sourcery.startHub" }
      },
      hoverProvider = true,
      inlayHintProvider = false,
      textDocumentSync = {
        change = 2,
        openClose = true,
        save = {
          includeText = true
        }
      },
      window = {
        workDoneProgress = true
      },
      workspace = {
        workspaceFolders = {
          changeNotifications = true,
          supported = true
        }
      }
    },
    stop = <function 50>,
    supports_method = <function 51>,
    workspace_did_change_configuration = <function 52>,
    workspace_folders = <table 11>
  }, {
    _on_attach = <function 53>,
    attached_buffers = { true,
      [78] = true
    },
    cancel_request = <function 54>,
    commands = {},
    config = {
      autostart = true,
      capabilities = {
        textDocument = <table 1>,
        window = <table 2>,
        workspace = {
          applyEdit = true,
          configuration = true,
          didChangeWatchedFiles = <table 3>,
          semanticTokens = <table 4>,
          symbol = <table 5>,
          workspaceEdit = <table 6>,
          workspaceFolders = true
        }
      },
      cmd = { "C:\\Users\\noahm\\AppData\\Local\\Programs\\Python\\Python310\\Scripts\\pyright-langserver.EXE", "--stdio", "--project", "C:/Users/noahm/.config/pyproject.toml" },
      cmd_cwd = "C:/Users/noahm/DocumentsNb/BA3/Algo-TPs",
      filetypes = { "python" },
      flags = {
        debounce_text_changes = 150
      },
      get_language_id = <function 55>,
      handlers = <table 7>,
      init_options = <table 8>,
      log_level = 2,
      message_level = 2,
      name = "pyright",
      on_attach = <function 56>,
      on_exit = <function 57>,
      on_init = <function 58>,
      root_dir = "C:/Users/noahm/DocumentsNb/BA3/Algo-TPs",
      settings = {
        pyright = {
          disableLanguageServices = true,
          disableOrganizeImports = true,
          reportMissingImports = "none",
          reportMissingModuleSource = "none",
          reportUndefinedVariable = "none"
        },
        python = {
          analysis = {
            autoImportCompletions = false,
            autoSearchPaths = false,
            diagnosticMode = "file",
            useLibraryCodeForTypes = true
          }
        }
      },
      single_file_support = true,
      workspace_folders = <12>{ {
          name = "C:/Users/noahm/DocumentsNb/BA3/Algo-TPs",
          uri = "file:///C:/Users/noahm/DocumentsNb/BA3/Algo-TPs"
        } },
      <metatable> = <table 10>
    },
    handlers = <table 7>,
    id = 4,
    initialized = true,
    is_stopped = <function 59>,
    messages = {
      messages = {},
      name = "pyright",
      progress = {},
      status = {}
    },
    name = "pyright",
    notify = <function 60>,
    offset_encoding = "utf-16",
    request = <function 61>,
    request_sync = <function 62>,
    requests = {},
    rpc = {
      is_closing = <function 63>,
      notify = <function 64>,
      request = <function 65>,
      terminate = <function 66>
    },
    server_capabilities = {
      callHierarchyProvider = true,
      codeActionProvider = {
        codeActionKinds = { "quickfix", "source.organizeImports" },
        workDoneProgress = true
      },
      completionProvider = {
        completionItem = {
          labelDetailsSupport = true
        },
        resolveProvider = true,
        triggerCharacters = { ".", "[", '"', "'" },
        workDoneProgress = true
      },
      declarationProvider = {
        workDoneProgress = true
      },
      definitionProvider = {
        workDoneProgress = true
      },
      documentHighlightProvider = {
        workDoneProgress = true
      },
      documentSymbolProvider = {
        workDoneProgress = true
      },
      executeCommandProvider = {
        commands = {},
        workDoneProgress = true
      },
      hoverProvider = {
        workDoneProgress = true
      },
      referencesProvider = {
        workDoneProgress = true
      },
      renameProvider = {
        prepareProvider = true,
        workDoneProgress = true
      },
      signatureHelpProvider = {
        triggerCharacters = { "(", ",", ")" },
        workDoneProgress = true
      },
      textDocumentSync = {
        change = 2,
        openClose = true,
        save = {
          includeText = false
        },
        willSave = false,
        willSaveWaitUntil = false
      },
      typeDefinitionProvider = {
        workDoneProgress = true
      },
      workspace = {
        workspaceFolders = {
          changeNotifications = true,
          supported = true
        }
      },
      workspaceSymbolProvider = {
        workDoneProgress = true
      }
    },
    stop = <function 67>,
    supports_method = <function 68>,
    workspace_did_change_configuration = <function 69>,
    workspace_folders = <table 12>
  }, {
    _on_attach = <function 70>,
    attached_buffers = { true,
      [78] = true
    },
    cancel_request = <function 71>,
    commands = {},
    config = {
      cmd = <function 72>,
      filetypes = { "python", "typescript", "go", "javascript", "lua", "html", "graphql", "markdown", "vue", "less", "json", "handlebars", "javascriptreact", "typescriptreact", "scss", "markdown.mdx", "jsonc", "yaml", "css" },
      flags = {
        debounce_text_changes = 250
      },
      get_language_id = <function 73>,
      name = "null-ls",
      on_attach = <function 74>,
      on_exit = <function 75>,
      on_init = <function 76>,
      root_dir = "C:/Users/noahm/DocumentsNb/BA3/Algo-TPs",
      settings = {}
    },
    handlers = {},
    id = 5,
    initialized = true,
    is_stopped = <function 77>,
    messages = {
      messages = {},
      name = "null-ls",
      progress = { {
          done = true,
          percentage = 50,
          title = "formatting"
        }, {
          done = true,
          percentage = 50,
          title = "formatting"
        }, {
          done = true,
          percentage = 0,
          title = "code_action"
        }, {
          done = true,
          percentage = 0,
          title = "code_action"
        }, {
          done = true,
          percentage = 0,
          title = "code_action"
        }, {
          done = true,
          percentage = 50,
          title = "formatting"
        }, {
          done = true,
          percentage = 50,
          title = "formatting"
        }, {
          done = true,
          percentage = 50,
          title = "formatting"
        }, {
          done = true,
          percentage = 50,
          title = "formatting"
        }, {
          done = true,
          percentage = 50,
          title = "formatting"
        }, {
          done = true,
          percentage = 50,
          title = "formatting"
        } },
      status = {}
    },
    name = "null-ls",
    notify = <function 78>,
    offset_encoding = "utf-16",
    request = <function 79>,
    request_sync = <function 80>,
    requests = {},
    rpc = {
      is_closing = <function 81>,
      notify = <function 82>,
      request = <function 83>,
      terminate = <function 84>
    },
    server_capabilities = {
      codeActionProvider = {
        resolveProvider = false
      },
      completionProvider = {
        allCommitCharacters = {},
        completionItem = {
          labelDetailsSupport = true
        },
        resolveProvider = false,
        triggerCharacters = { ".", ":", "-" }
      },
      documentFormattingProvider = true,
      documentRangeFormattingProvider = true,
      executeCommandProvider = {
        commands = { "NULL_LS_CODE_ACTION" }
      },
      hoverProvider = true,
      textDocumentSync = {
        change = 1,
        openClose = true,
        save = {
          includeText = true
        }
      }
    },
    stop = <function 85>,
    supports_method = <function 86>,
    workspace_folders = { {
        name = "C:/Users/noahm/DocumentsNb/BA3/Algo-TPs",
        uri = "file:///C:/Users/noahm/DocumentsNb/BA3/Algo-TPs"
      } }
  } }