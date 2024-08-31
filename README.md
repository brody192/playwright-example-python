# This example is to be used with the [Browserless template](https://railway.app/template/browserless)

Create a reference variable on your Railway service that you deploy your app to -

```shell
BROWSER_PLAYWRIGHT_ENDPOINT=${{Browserless.BROWSER_PLAYWRIGHT_ENDPOINT}}
```

</br>

Then use `os.environ['BROWSER_PLAYWRIGHT_ENDPOINT']` in code -

### Before

```python
browser = await p.chromium.launch()
```

### After

```python
browser = await p.chromium.connect(os.environ['BROWSER_PLAYWRIGHT_ENDPOINT'])
```

The rest of your code remains the same with no other changes required.