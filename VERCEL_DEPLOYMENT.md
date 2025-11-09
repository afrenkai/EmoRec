# Vercel Deployment Guide

## Overview
This project is configured to deploy a FastAPI backend to Vercel using serverless functions.

## Files Created for Vercel Deployment

1. **`vercel.json`** - Vercel configuration file
2. **`api/index.py`** - Vercel entrypoint that exports the FastAPI app
3. **`.vercelignore`** - Files to exclude from deployment

## Deployment Steps

### Option 1: Deploy via Vercel CLI

1. Install Vercel CLI:
   ```bash
   npm i -g vercel
   ```

2. Login to Vercel:
   ```bash
   vercel login
   ```

3. Deploy:
   ```bash
   vercel
   ```

4. For production deployment:
   ```bash
   vercel --prod
   ```

### Option 2: Deploy via GitHub Integration

1. Push your code to GitHub
2. Go to [vercel.com](https://vercel.com)
3. Click "Import Project"
4. Select your repository
5. Vercel will automatically detect the configuration

## Environment Variables

Make sure to set these environment variables in your Vercel project settings:

- `SPOTIFY_CLIENT_ID` - Your Spotify API client ID
- `SPOTIFY_CLIENT_SECRET` - Your Spotify API client secret
- `GENIUS_ACCESS_TOKEN` - Your Genius API access token (optional)
- Any other environment variables your app needs

### Setting Environment Variables in Vercel:

1. Go to your project settings on Vercel
2. Navigate to "Environment Variables"
3. Add each variable with its value
4. Choose the appropriate environments (Production, Preview, Development)

## Important Notes

### Serverless Limitations

1. **Cold Starts**: First request may be slower due to initialization
2. **Execution Time**: Vercel free tier has a 10-second execution limit (Pro: 60s, Enterprise: 900s)
3. **File System**: Read-only file system except for `/tmp` directory
4. **Memory**: Limited memory based on your Vercel plan

### Model Files

If your embedding service uses large model files (sentence-transformers), consider:

1. **Using smaller models** for faster cold starts
2. **Caching models** in `/tmp` directory
3. **Using external model hosting** services
4. **Upgrading to Vercel Pro** for better performance

### API Endpoints

After deployment, your API will be available at:
- Production: `https://your-project.vercel.app/`
- API docs: `https://your-project.vercel.app/docs`
- Health check: `https://your-project.vercel.app/health`
- Playlist generation: `https://your-project.vercel.app/api/v1/generate-playlist`

## Frontend Deployment

If you want to deploy the frontend separately or together:

### Separate Deployment (Recommended):
1. Deploy backend using the current configuration
2. Create a separate Vercel project for the Next.js frontend
3. Update frontend environment variables to point to backend URL

### Monorepo Deployment:
Update `vercel.json` to include frontend build configuration. This is more complex and may require additional setup.

## Troubleshooting

### Issue: "No Python entrypoint found"
- Ensure `api/index.py` exists and exports `app`
- Check `vercel.json` points to correct build source

### Issue: Import errors
- Check `PYTHONPATH` is set in `vercel.json`
- Verify all dependencies are in `requirements.txt`

### Issue: Timeout errors
- Consider optimizing model loading
- Use smaller models
- Implement caching strategies
- Upgrade Vercel plan if needed

### Issue: Environment variables not working
- Ensure variables are set in Vercel project settings
- Redeploy after adding variables
- Check variable names match exactly

## Testing Locally

Test the Vercel configuration locally:

```bash
vercel dev
```

This starts a local development server that mimics Vercel's serverless environment.

## Monitoring

Monitor your deployment:
- Check Vercel dashboard for logs
- Use Vercel Analytics for performance insights
- Set up error tracking (Sentry, etc.)

## Performance Optimization

1. **Reduce Cold Start Time**:
   - Minimize dependencies
   - Use lightweight models
   - Implement lazy loading

2. **Caching**:
   - Cache API responses
   - Store frequently used data in memory
   - Use Vercel's Edge Cache

3. **Database/Storage**:
   - Use external databases (not local files)
   - Consider Redis for caching
   - Use object storage for large files

## Additional Resources

- [Vercel Python Documentation](https://vercel.com/docs/functions/serverless-functions/runtimes/python)
- [FastAPI on Vercel](https://vercel.com/docs/frameworks/fastapi)
- [Vercel CLI Documentation](https://vercel.com/docs/cli)
